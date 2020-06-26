# This is for testing on laptop but the real client code is in the android app
import socket

soc = socket.socket()
soc.connect(('localhost',9999))


filename = input('Enter filename to send: ')
with soc:
    with open(filename, 'rb') as file:
        sendfile = file.read()
    soc.sendall(sendfile)
    print('file sent')