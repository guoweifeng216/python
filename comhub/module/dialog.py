# -*- coding:utf-8 -*-
import os
import yaml
import locale
import serial
from serial.tools.list_ports import comports
from ui.ui_dialog import UiDialogSerial
from ui.ui_xmodem import UiDialogXmodem
from module.com import ThreadXmodem
from PyQt4.QtGui import QDialog, QMessageBox, QMainWindow, QWidget, QFileDialog


# noinspection PyTypeChecker
class DialogXmodem(QDialog):
    def __init__(self, session):
        super(DialogXmodem, self).__init__()

        self.session = session
        self.serial = session.envs.get("SERIAL")

        self.file = os.path.join('conf', 'xmodem.yaml')
        self.packages = 0
        self.xmodem = None
        self.dialog = UiDialogXmodem()

        self.setup_ui()

        self.conf = yaml.load(open(self.file).read()) if os.path.exists(self.file) else dict()
        self.dialog.lineEdit_image.setText(self.conf.get("FILE", ""))
        self.dialog.lineEdit_cmd.setText(self.conf.get("COMMAND", ""))
        self.dialog.lineEdit_timeout.setText(self.conf.get("TIMEOUT", "3000"))

    def setup_ui(self):
        self.dialog.setup_ui(self)
        self.dialog.buttonBox.accepted.connect(self.start)
        self.dialog.buttonBox.rejected.connect(self.cancel)
        self.dialog.pushButton_image.clicked.connect(self.open_file)

    def open_file(self):
        dirs = os.path.dirname(self.conf.get("FILE", __file__))
        # noinspection PyCallByClass
        path = QFileDialog.getOpenFileName(self, 'Open file', dirs)
        if path:
            self.dialog.lineEdit_image.setText(path)

    def cancel(self):
        if self.xmodem and self.xmodem.isRunning():
            QMessageBox(self).warning(self, "Warning",
                                      "\nXmodem is running\n",
                                      QMessageBox.Ok)
            return
        self.reject()

    def is_running(self):
        if self.xmodem and self.xmodem.isRunning():
            return True
        return False

    def start(self):
        if self.xmodem and self.xmodem.isRunning():
            QMessageBox(self).warning(self, "Warning",
                                      "\nXmodem is running\n",
                                      QMessageBox.Ok)
            return

        cmd = str(self.dialog.lineEdit_cmd.text())
        path = str(self.dialog.lineEdit_image.text())
        timeout = int(self.dialog.lineEdit_timeout.text())
        if not os.path.exists(path):
            QMessageBox(self).warning(self, "Warning",
                                      "\npath: '{}' is non-existent\n".format(path),
                                      QMessageBox.Ok)
            return

        self.conf['FILE'] = path
        self.conf['TIMEOUT'] = str(timeout)
        self.conf['COMMAND'] = cmd
        yaml.dump(self.conf, open(self.file, "w"))

        self.packages = (os.path.getsize(path) + 128 - 1) / 128
        self.dialog.progress_bar.setMinimum(0)
        self.dialog.progress_bar.setMaximum(self.packages)
        self.dialog.progress_bar.setValue(0)
        self.dialog.label_total.setText("Total: {}".format(self.packages))
        self.process(self.packages, 0, 0)

        self.xmodem = ThreadXmodem(self.session, cmd, timeout, path)
        self.xmodem.procUpdate.connect(self.process)
        self.xmodem.doneUpdate.connect(self.completed)
        self.xmodem.start()
        self.dialog.pushButton_start.setEnabled(False)

    def completed(self, status):
        self.dialog.pushButton_start.setEnabled(True)

        if status:
            self.accept()

    # noinspection PyUnusedLocal
    def process(self, packages, success, error):
        if error:
            self.dialog.label_error.setText("Error: {}".format(error))
        self.dialog.label_success.setText("Success: {}".format(success))
        self.dialog.progress_bar.setValue(packages)


class DialogSerial(QDialog):
    BAUDRATES = (115200, 921600)
    FLOWCONTROLS = ("None", "RTS/CTS", "XON/XOFF")
    PREFIX = ("None", "DATA+TIME")

    def __init__(self):
        super(DialogSerial, self).__init__()

        self.encoding = locale.getpreferredencoding()
        self.file = os.path.join('conf', 'default.yaml')

        # Init Dialog UI
        self.dialog = UiDialogSerial()
        self.setup_ui()

        # For serial
        self.serial = serial.Serial()

        self.envs = dict()
        self.common = dict()
        self.sessions = yaml.load(open(self.file).read()) if os.path.exists(self.file) else dict()

        self.init()

    def setup_ui(self):
        self.dialog.setup_ui(self)
        self.dialog.buttonBox.accepted.connect(self.open)
        self.dialog.buttonBox.rejected.connect(self.reject)

    def init(self):
        for i, baudrate in enumerate(self.BAUDRATES):
            self.dialog.comboBox_baudrate.addItem(str(baudrate))

        for i, bytesize in enumerate(self.serial.BYTESIZES):
            self.dialog.comboBox_dataBits.addItem(str(bytesize))
            self.dialog.comboBox_dataBits.setCurrentIndex(i)

        for i, stopbits in enumerate(self.serial.STOPBITS):
            self.dialog.comboBox_stopBits.addItem(str(stopbits))

        for i, parity in enumerate(self.serial.PARITIES):
            self.dialog.comboBox_parity.addItem(parity)

        for i, flowcontrol in enumerate(self.FLOWCONTROLS):
            self.dialog.comboBox_flowControl.addItem(flowcontrol)

        for n, line_prefix in enumerate(self.PREFIX):
            self.dialog.comboBox_linePrefix.addItem(line_prefix)

        self.dialog.comboBox_port.currentIndexChanged.connect(self.setup_serial)
        for i, (port, _, _) in enumerate(sorted(comports())):
            self.dialog.comboBox_port.addItem(str(port))

        # Set port as last session
        index = self.dialog.comboBox_port.findText(self.sessions.get("LASTSESSION", ""))
        if index != -1:
            self.dialog.comboBox_port.setCurrentIndex(index)

        # Set common
        common = self.sessions.get("COMMON", dict())
        index = self.dialog.comboBox_linePrefix.findText(common.get("PREFIX", "None"))
        self.dialog.comboBox_linePrefix.setCurrentIndex(index)
        self.dialog.lineEdit_logPath.setText(common.get("LOGPATH", ""))
        self.dialog.lineEdit_logSize.setText(str(common.get("LOGMAXSIZE", "")))
        self.dialog.lineEdit_textLine.setText(str(common.get("TEXTMAXLINE", "")))

    def open(self):
        try:
            self.setup_dialog()
            self.serial.open()
        except serial.SerialException as e:
            msg = "\n{}\n".format(eval(repr(e.message).replace('\\\\', '\\')))
            QMessageBox(self).warning(self, "Warning",
                                      msg.decode(self.encoding),
                                      QMessageBox.Ok)
        else:
            # update yaml
            self.sessions[self.serial.port] = self.envs
            self.sessions["COMMON"] = self.common
            self.sessions["LASTSESSION"] = self.serial.port

            yaml.dump(self.sessions, open(self.file, "w"))

            self.envs.update(self.common)
            self.envs["SERIAL"] = self.serial

            self.accept()

    def setup_serial(self, index):
        name = self.dialog.comboBox_port.itemText(index)
        session = self.sessions.get(str(name), dict())

        index = self.dialog.comboBox_baudrate.findText(str(session.get("BAUDRATE", 115200)))
        self.dialog.comboBox_baudrate.setCurrentIndex(index)

        index = self.dialog.comboBox_dataBits.findText(str(session.get("BYTESIZE", 8)))
        self.dialog.comboBox_dataBits.setCurrentIndex(index)

        index = self.dialog.comboBox_stopBits.findText("{:g}".format(session.get("STOPBITS", 1)))
        self.dialog.comboBox_stopBits.setCurrentIndex(index)

        index = self.dialog.comboBox_parity.findText(session.get("PARITY", "N"))
        self.dialog.comboBox_parity.setCurrentIndex(index)

        index = self.dialog.comboBox_flowControl.findText(session.get("FLOWCONTROL", "None"))
        self.dialog.comboBox_flowControl.setCurrentIndex(index)

    def setup_dialog(self):
        # Serial basic setup
        self.serial.port = str(self.dialog.comboBox_port.currentText())
        self.serial.baudrate = int(self.dialog.comboBox_baudrate.currentText())
        self.serial.bytesize = int(self.dialog.comboBox_dataBits.currentText())
        self.serial.stopbits = float(self.dialog.comboBox_stopBits.currentText())
        self.serial.parity = str(self.dialog.comboBox_parity.currentText())

        # Flow control setup
        flowcontrol = str(self.dialog.comboBox_flowControl.currentText())
        self.serial.rtscts = False
        self.serial.xonxoff = False
        if flowcontrol == "RTS/CTS":
            self.serial.rtscts = True
        elif flowcontrol == "XON/XOFF":
            self.serial.xonxoff = True

        # Serial envs
        self.envs["BAUDRATE"] = self.serial.baudrate
        self.envs["BYTESIZE"] = self.serial.bytesize
        self.envs["STOPBITS"] = self.serial.stopbits
        self.envs["PARITY"] = self.serial.parity
        self.envs["FLOWCONTROL"] = flowcontrol

        # Common envs
        log_max_line = self.dialog.lineEdit_textLine.text()
        if log_max_line == "":
            log_max_line = 1000
        self.common["TEXTMAXLINE"] = int(log_max_line)
        self.common["PREFIX"] = str(self.dialog.comboBox_linePrefix.currentText())
        self.common["LOGPATH"] = str(self.dialog.lineEdit_logPath.text())
        log_max_size = self.dialog.lineEdit_logSize.text()
        if log_max_size == "":
            log_max_size = 0
        self.common["LOGMAXSIZE"] = float(log_max_size)
