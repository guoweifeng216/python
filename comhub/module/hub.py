import os
import time
import select
import socket
import paramiko
import threading
from PyQt4.QtCore import QThread, QMutex, pyqtSignal


def debug(msg):
    if True:
        print("[{}] {}".format(time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time())),
                               msg))


class Server(paramiko.ServerInterface):
    """SSH Server class"""
    def __init__(self, username=None, password=None):
        self.event = threading.Event()
        self.username = username
        self.password = password

    def check_channel_request(self, kind, chanid):
        """Determine if a channel request of a given type will be granted"""
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        """Determine if a given username and password supplied by the client is
        acceptable for use in authentication."""
        if username == self.username and password == self.password:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED


# noinspection PyTypeChecker
class ThreadHub(QThread):
    recvUpdate = pyqtSignal(str)
    connUpdate = pyqtSignal(str)

    # Up/Down/Left/Right/Tab
    # Insert/Delete/Home/End/PageUp/PageDown
    # F1~F12
    KEY_IGNORE = ["\x1b[A", "\x1b[B", "\x1b[D", "\x1b[C", "\t",
                  "\x1b[2~", "\x1b[3~", "\x1b[1~", "\x1b[4~", "\x1b[5~", "\x1b[6~",
                  "\x1bOP", "\x1bOQ", "\x1bOR", "\x1bOS",
                  "\x1b[15~", "\x1b[17~", "\x1b[18~", "\x1b[19~",
                  "\x1b[20~", "\x1b[21~", "\x1b[23~", "\x1b[24~"]

    def __init__(self, envs):
        super(ThreadHub, self).__init__()
        self.serial = envs.get('SERIAL')
        self.port = envs.get('PORT')
        self.host = self.get_host_ip()
        self.mutex = QMutex()
        self.client = dict()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.host_key = paramiko.RSAKey(filename=os.path.join('key', 'id_rsa'))
        self.server = Server(username="root", password="nvme")
        self.sock.listen(32)
        debug('[+] Listening {}:{} ...'.format(self.host, self.port))

    @staticmethod
    def get_host_ip():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.connect(('8.8.8.8', 80))
            return sock.getsockname()[0]
        except socket.error:
            return "0.0.0.0"
        finally:
            sock.close()

    def run(self):
        while True:
            rlist, _, _ = select.select([self.sock] + self.client.keys(), [], [])

            try:
                self.sock.fileno()
            except socket.error:
                self.close(self.client.keys())
                debug("[-] Terminate {}:{}".format(self.host, self.port))
                break

            for sock in rlist:
                if sock is self.sock:
                    conn, (ip, port) = self.sock.accept()
                    debug('[+] {}:{} Connected!'.format(ip, port))

                    try:
                        session = paramiko.Transport(conn)
                        session.add_server_key(self.host_key)
                        session.start_server(server=self.server)
                        sock = session.accept(60)
                        if not sock:
                            debug('[-] {}:{} Authenticate fail!'.format(ip, port))
                            continue
                    except paramiko.SSHException as e:
                        debug(e)
                        continue

                    debug('[+] {}:{} Authenticated!'.format(ip, port))
                    self.client[sock] = (ip, port)
                    self.connUpdate.emit(str(len(self.client)))
                else:
                    recv = sock.recv(4096)
                    if recv == "":
                        # Remove disconnected socket
                        self.close([sock])
                        self.connUpdate.emit(str(len(self.client)))
                    else:
                        # Ignore some keys
                        if recv in self.KEY_IGNORE:
                            continue
                        self.recvUpdate.emit(recv)

    def send(self, data):
        data = unicode(data).encode('utf-8')

        self.mutex.lock()
        try:
            for sock in self.client.keys():
                try:
                    sock.send(data)
                except socket.error as e:
                    debug(e)
        finally:
            self.mutex.unlock()

    def close(self, socks):
        self.mutex.lock()
        try:
            for sock in socks:
                ip, port = self.client[sock]
                debug('[-] {}:{} Disconnected!'.format(ip, port))
                sock.close()
                del self.client[sock]
        finally:
            self.mutex.unlock()

    def terminate(self):
        self.sock.close()
        self.wait()
