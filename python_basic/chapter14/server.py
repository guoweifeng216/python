#coding:utf-8

import socket
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    sock.bind((host, 8001))
    sock.listen(5)
    print(host)
    while True:
        connection,address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            print(buf)
            if buf == b'1':
                connection.send('welcome to server!'.encode())
            else:
                connection.send('please go out!'.encode())
        except socket.timeout:
            print( 'time out')

        connection.close()