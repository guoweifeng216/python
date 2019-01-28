import os
import time
from PyQt4.QtCore import pyqtSignal, QObject


class Log(QObject):
    sizeUpdate = pyqtSignal(str)
    pathUpdate = pyqtSignal(str)

    def __init__(self, name, envs):
        super(Log, self).__init__()
        self.envs = envs

        self.file = None
        self.size = 0
        self.index = 0
        self.handle = None
        self.enable = True if self.envs.get("LOGPATH") else False

        if self.enable:
            self.time = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime(time.time()))
            self.path = os.path.join(self.envs.get("LOGPATH"),
                                     "{}_{}".format(name, self.envs.get("BAUDRATE")))
            if not os.path.exists(self.path):
                os.makedirs(self.path)

    def open(self):
        if not self.handle and self.enable:
            self.file = os.path.join(self.path, "{}.{}.log".format(self.time, self.index))
            self.handle = open(self.file, 'w')
            self.size = 0
            self.index += 1

            self.envs["LOGSIZE"] = 0.0

            self.sizeUpdate.emit("{}/{}".format(self.envs["LOGSIZE"], self.envs["LOGMAXSIZE"]))
            self.pathUpdate.emit(self.file)

    def close(self):
        if self.handle and self.enable:
            self.handle.close()
            self.handle = None
            self.sizeUpdate.emit("")
            self.pathUpdate.emit("")

    def reload(self):
        if self.handle and self.enable:
            self.close()
            self.open()

    def write(self, data):
        if self.handle and self.enable:
            self.handle.write(data)
            self.handle.flush()

            self.size += len(data)
            self.envs["LOGSIZE"] = float(self.size) / 0x100000
            self.sizeUpdate.emit("{:.1f}/{:.1f}".format(self.envs["LOGSIZE"],
                                                        self.envs["LOGMAXSIZE"]))
            if self.envs["LOGSIZE"] >= self.envs["LOGMAXSIZE"]:
                self.reload()
