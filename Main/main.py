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
import sys
import cv2
import os

sys.path.insert(1, '../monodepth2/')
from test_simple import *

sys.path.insert(1, '../Open3D-master/examples/Python/ReconstructionSystem')
from run_system import *



class Main():

    def __init__(self):
        super().__init__()
        # get the hostname 
        self.host = socket.gethostname() 
        # initiate port number above 1024
        self.port = 5000
    
    def create_server(self):
        # get instance
        self.server_socket = socket.socket()

        # bind host address and port together
        self.server_socket.bind(('',port))
        
        return


    def start_server(self):
        # can listen to 10 clients simultaneously
        self.server_socket.listen(10)

        print('waiting for connection...')

        with self.server_socket:

            # accept new connection
            self.con, self.addr = self.server_socket.accept()
            print('server connected to : ', self.addr)

            self.get_data_from_client()
        return
    

    def get_data_from_client(self):

        with self.con:
            # Get the name of the file which you intend to save
            self.savefilename = input('Enter filename to save as : ')

            # Reecieving video from the mobile phone
            with open(self.savefilename, 'wb') as file:
                
                while True:
                    # receive data stream. it won't accept data packet greater than 4096 bytes
                    recvfile = self.con.recv(4096)
                
                    if not recvfile:
                        print("recvfile is 'None' ")
                        break
                
                    file.write(recvfile)

                file.close()
            
            print('file saved')

        return
    
    def process_data(self):

        # Processing the data and getting the desired output 

        # Make video into images and store in 'rgb_images' folder

        if not os.path.exists('dataset'):
            os.makedirs('dataset')

        if not os.path.exists('./dataset/image'):
            os.makedirs('./dataset/image')
        
        vidcap = cv2.VideoCapture(savefilename)
        success, image = vidcap.read()

        # Saving space while saving
        params = list()
        params.append(cv2.CV_IMWRITE_PNG_COMPRESSION)
        params.append(8)
        
        count = 0
        while success:
            
            cv2.imwrite("./dataset/image/frame%d.png" % count, image, params)     # save frame as PNG file      
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1


    def run_algorithm(self):

        # Generate depth maps from rbg images
         
        args = parse_args()
        test_simple(args)


        # Run open3d on rgb+depth maps to get the point cloud output

        return

    
    def send_data_to_client(self):





        # Closing connection
        self.con.close()
        return



if __name__=='__main__':

    proj = Main()

    proj.create_server()
    proj.start_server()
    data = proj.get_data_from_client()
    proj.run_algorithm()
    proj.send_data_to_client()






    
    


        
    
       

    
    