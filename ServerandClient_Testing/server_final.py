import socket


host = socket.gethostname()
port = 5000
soc = socket.socket()

soc.bind(('',port))
soc.listen(10)

print('waiting for connection...')

# To receive video from mobile
def recieve_video():
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


            # send back the same file

            

        con.close()

# To send point cloud to mobile
def send_pointcloud():
    with soc:
        con,addr = soc.accept()
        print('server connected to',addr)
        
        filename = "./pcd.ply"
        with soc:
            with open(filename, 'rb') as file:
                sendfile = file.read(4096)
                # l = f.read(1024)
                print("Read file")
                while (sendfile):
                    con.send(sendfile)
                    print("sending .....")
                    sendfile = file.read(4096)
            # soc.sendall(sendfile)
            print('file sent')
    
        con.close()

