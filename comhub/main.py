import re
import sys
import ctypes
from ui.ui_main import UiMainWindow
from module.log import Log
from module.text import Text
from module.hub import ThreadHub
from module.com import ThreadSerial
from module.dialog import DialogSerial, DialogXmodem
from PyQt4.QtGui import QFont, QApplication, QMainWindow, QMessageBox, QDialog

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("COMHUB")


class Class(object):
    pass


class MainWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super(MainWindow, self).__init__(parent)

        self.main = UiMainWindow()
        self.setup_ui()

        self.session = dict()
        self.clipboard = app.clipboard()

    def setup_ui(self):
        self.main.setup_ui(self)

        self.main.action_open.triggered.connect(self.open)
        self.main.action_close.triggered.connect(self.close)
        self.main.action_trans.triggered.connect(self.xmodem)

    def open(self):
        dialog = DialogSerial()

        if QDialog.Accepted == dialog.exec_():
            name = dialog.serial.port
            if name in self.session:
                msg = "\nTab '{}' is open\n\nPlease close it and try again\n".format(name)
                QMessageBox(self).warning(self, "Warning", msg, QMessageBox.Ok)

            # Update envs
            session = Class()
            session.envs = dialog.envs
            session.envs["PORT"] = 10000 + int(re.findall(r"(\d+)", name)[0])

            # Start Log object
            session.log = Log(name, session.envs)
            self.main.action_reload.triggered.connect(session.log.reload)

            # Add tab
            session.tab = self.main.add_tab(name, session.envs)
            session.tab.install_event_filter(self)
            session.log.pathUpdate.connect(session.tab.update_status_path)
            session.log.sizeUpdate.connect(session.tab.update_status_size)
            session.log.open()

            # Add text functions
            session.text = Text(session, self.clipboard)

            # Start COM/HUB Thread
            session.hub = ThreadHub(session.envs)
            session.serial = ThreadSerial(session.envs)

            session.serial.dataUpdate.connect(session.hub.send)
            session.serial.dataUpdate.connect(session.text.append)
            session.hub.recvUpdate.connect(session.serial.write)
            session.hub.connUpdate.connect(session.tab.update_status_count)
            session.text.dataUpdate.connect(session.serial.write)

            session.serial.start()
            session.hub.start()

            self.session[name] = session

    def xmodem(self):
        name = self.main.get_tab_cur_name()
        if name in self.session:
            self.session[name].xmodem = DialogXmodem(self.session[name])
            self.session[name].xmodem.show()

    def close(self, name=None, force=False):
        name = name if name else self.main.get_tab_cur_name()

        # Terminate threads
        if name in self.session:
            if hasattr(self.session[name], 'xmodem') and self.session[name].xmodem.isVisible():
                if force:
                    self.session[name].xmodem.reject()
                else:
                    msg = "\nTab '{}' xmodem is running\n\n" \
                          "Please close it and try again\n".format(name)
                    QMessageBox(self).warning(self, "Warning", msg, QMessageBox.Ok)
                    return

            self.session[name].hub.terminate()
            self.session[name].log.close()
            self.session[name].serial.terminate()
            self.main.remove_tab(name)
            del self.session[name]

    def terminate(self, force=True):
        for name in self.session.keys():
            self.close(name, force)

    def eventFilter(self, obj, event):
        for name in self.session.keys():
            if obj is self.session[name].tab.text:
                return self.session[name].text.event_filter(obj, event)

        return False

    def closeEvent(self, event):
        self.terminate()
        event.accept()


if __name__ == '__main__':
    FONT = QFont()
    FONT.setFamily("DejaVu Sans Mono")
    FONT.setPointSize(9)

    APP = QApplication(sys.argv)
    APP.setFont(FONT)

    MAIN = MainWindow(APP)
    MAIN.show()

    APP.exec_()
    MAIN.terminate()

    sys.exit(0)
