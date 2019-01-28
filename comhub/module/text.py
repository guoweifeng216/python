import re
import time
from PyQt4.QtCore import QEvent, Qt, pyqtSignal, QObject, QString


KEY_BACKSPACE = "\x08"


class CMD(object):
    def __init__(self, tab, sender):
        self.tab = tab
        self.sender = sender

    def backspace(self, count=1):
        if count:
            self.tab.backspace(count)

    def send(self, data):
        if data:
            self.sender.emit(data)


class Text(QObject):
    dataUpdate = pyqtSignal(str)

    KEY_IGNORE = [Qt.Key_Left, Qt.Key_Right, Qt.Key_Tab, Qt.Key_Delete]

    def __init__(self, session, clipboard):
        super(Text, self).__init__()
        self.tab = session.tab
        self.log = session.log
        self.clipboard = clipboard

        self.cmd = CMD(self.tab, self.dataUpdate)

        self.data_time = session.envs.get('PREFIX') is "DATA+TIME"

    def append(self, data):
        data = unicode(data).encode('utf-8')

        # If it is a backspace, delete previous character and return
        if KEY_BACKSPACE in data:
            self.cmd.backspace(data.count(" "))
            return

        # Add time stamp to every line
        if self.data_time:
            data = data.replace("\n", "\n{}".format(self.time_stamp()))

        # Delete Non-printable Characters
        # noinspection Annotator
        data = re.sub('[\x00-\x09|\x0b-\x0c|\x0e-\x1f|\x7f]', '.', data)

        # Send to text edit
        self.tab.append(data)

        # Log record
        self.log.write(data)

    @staticmethod
    def time_stamp():
        return time.strftime("[%m-%d %H:%M:%S] ", time.localtime(time.time()))

    def paste(self, obj):
        # Get only one line to avoid too many commands send to serial
        if obj.canPaste:
            data = self.clipboard.text().split("\n")[0]
            self.cmd.send(data)

    def event_filter(self, obj, event):
        # Mouse Press Event
        if event.type() == QEvent.MouseButtonPress and event.buttons() == Qt.RightButton:
            self.paste(obj)
            return True

        # Key Press Event
        if event.type() == QEvent.KeyPress:
            if event.modifiers() == Qt.ShiftModifier:
                if event.key() == Qt.Key_Insert:
                    self.paste(obj)
                    return True
            elif event.modifiers() == Qt.ControlModifier:
                if event.key() == Qt.Key_V:
                    self.paste(obj)
                    return True
            elif event.key() == Qt.Key_Backspace:
                self.cmd.send(KEY_BACKSPACE)
                return True
            elif event.key() in (Qt.Key_Enter, Qt.Key_Return):
                self.cmd.send("\r")
                return True
            elif event.key() in self.KEY_IGNORE:
                return True
            elif event.text():
                self.cmd.send(event.text())
                return True
            return False

        return False
