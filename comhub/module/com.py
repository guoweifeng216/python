import time
from xmodem import XMODEM
from PyQt4.QtCore import QThread, pyqtSignal, QMutex


def debug(msg):
    if True:
        print("[{}] {}".format(time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time())),
                               msg))


class ThreadSerial(QThread):
    dataUpdate = pyqtSignal(str)

    def __init__(self, envs):
        super(ThreadSerial, self).__init__()
        self.serial = envs.get('SERIAL')
        self.mutex = QMutex()
        self.exit = False

    def run(self):
        debug("[+] Listening {}".format(self.serial.port))

        while not self.exit:
            if self.mutex.tryLock(100):
                try:
                    data = self.serial.read_all()
                finally:
                    self.mutex.unlock()

                if data:
                    self.dataUpdate.emit(data)
            time.sleep(0.001)

    def pause(self, timeout=1000):
        return self.mutex.tryLock(timeout)

    def resume(self):
        self.mutex.unlock()

    def read_no_wait(self):
        data = self.serial.read_all()
        self.dataUpdate.emit(data)
        return data

    def write_no_wait(self, data):
        self.serial.write(unicode(data).encode('utf-8'))

    def write(self, data):
        if self.mutex.tryLock(100):
            try:
                self.serial.write(unicode(data).encode('utf-8'))
            finally:
                self.mutex.unlock()

    def terminate(self, timeout=1000):
        debug("[-] Terminate {}".format(self.serial.port))
        self.exit = True
        if not self.wait(timeout):
            QThread.terminate(self)
        self.serial.close()


class ThreadXmodem(QThread):
    procUpdate = pyqtSignal(int, int, int)
    doneUpdate = pyqtSignal(bool)

    def __init__(self, session, cmd, timeout, path):
        super(ThreadXmodem, self).__init__()
        self.serial = session.envs.get('SERIAL')
        self.tSerial = session.serial
        self.cmd = cmd
        self.path = path
        self.timeout = float(timeout) / 1000
        self.modem = None
        self.status = False

    # noinspection PyUnusedLocal
    def getc(self, size, timeout=1):
        return self.serial.read(size)

    # noinspection PyUnusedLocal
    def putc(self, data, timeout=1):
        self.serial.write(data)

    def callback(self, packages, success, error):
        self.procUpdate.emit(packages, success, error)

    def run(self):
        try:
            if self.tSerial.pause():
                try:
                    if self.cmd:
                        # Send command and wait for ACK(\x15)
                        self.tSerial.write_no_wait("{}\n".format(self.cmd))
                        tm_bgn = time.time()
                        while time.time() - tm_bgn < self.timeout:
                            data = self.tSerial.read_no_wait()
                            if data and data in ["\x15", "C"]:
                                break
                            time.sleep(0.2)
                        else:
                            return

                    # Start xmodem send
                    self.modem = XMODEM(self.getc, self.putc, mode='xmodem')
                    with open(self.path, 'rb') as fd:
                        self.status = self.modem.send(fd, callback=self.callback)
                finally:
                    self.tSerial.resume()
        finally:
            self.doneUpdate.emit(self.status)

    def terminate(self, timeout=1000):
        if not self.wait(timeout):
            print("[-] Terminate XMODEM Thread")
            QThread.terminate(self)
