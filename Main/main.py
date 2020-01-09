'''
Responsible for automating all the stuff : 
Laptop is the server and mobile is the client

1. Running server to fetch video
2. Running scripts for generating depth maps from the video
3. Running open3d to generate point cloud based on the rgbd data
4. Sending back the video to the mobile 

'''


'''
1. Server 

Stays up until manually stopped

[a] Waits for client (android app) and gets the video and retains the connection for sending back the video
[b] All the calls made in within the server 

'''


import socket

# get the hostname
host = socket.gethostname() 
# initiate port number above 1024
port = 5000

# get instance
server_socket = socket.socket()

# bind host address and port together
server_socket.bind(('',port))

# can listen to 10 clients simultaneously
server_socket.listen(10)

print('waiting for connection...')

with server_socket:

    # accept new connection
    con, addr = server_socket.accept()
    print('server connected to',addr)
    
    with con:
        # Get the name of the file which you intend to save
        savefilename = input('Enter filename to save as : ')


        with open(savefilename, 'wb') as file:
            
            while True:
                # receive data stream. it won't accept data packet greater than 4096 bytes
                recvfile = con.recv(4096)
            
                if not recvfile:
                    print("recvfile is 'None' ")
                    break
            
                file.write(recvfile)
        
        print('file saved')
    
    
        '''
        2. Generate depth maps from the video recieved
        
        Using monodepth2 to get depth maps from rgb images
        '''
        




        '''
        3. Generate point cloud using open3d and rgbd data
        '''
    
    
        '''
        4. Send the point cloud file to the mobile
        '''
    
    
    # Closing connection
    con.close()