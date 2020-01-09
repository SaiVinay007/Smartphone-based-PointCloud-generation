import socket


host = socket.gethostname()
port = 5000
soc = socket.socket()

soc.bind(('',port))
soc.listen(2)

print('waiting for connection...')
with soc:
    con,addr = soc.accept()
    print('server connected to',addr)
    with con:
        savefilename = input('Enter filename to save as : ')

        with open(savefilename, 'wb') as file:
            while True:
                print("Going ...")
                recvfile = con.recv(4096)
                if not recvfile:
                    print("not recvfile :( ")
                    break
                file.write(recvfile)
                print("Recieving...")
        print('file saved')
    con.close()