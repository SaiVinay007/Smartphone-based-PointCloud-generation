import cv2
import os

if not os.path.exists('depth_new'):
    os.makedirs('depth_new')

if not os.path.exists('image_new'):
    os.makedirs('image_new')

Data_root = "/home/saivinay/Documents/ADRIN_INTERN/datasets/dataset/"
# Destination_path = "/home/saivinay"


depth_path = './depth'
image_path = './image'

image_paths = os.listdir(image_path)
image_paths.sort( key= lambda x: int(x[5:-4]))

depth_paths = os.listdir(depth_path)
depth_paths.sort( key= lambda x: int(x[5:-9]))


# num=0
# for i in image_paths:
#     # print(i)
#     path = Data_root+'/image/'+i
#     # print(path)
#     image = cv2.imread(path)
#     # print(image)
#     res_img = cv2.resize(image, (640, 480))
#     cv2.imwrite(Data_root+'/image_new/'+'frame'+str(num)+'.png', res_img )
#     num+=1
    
num=0
for i in depth_paths:
    # print(i)
    path = Data_root+'/depth/'+i
    # print(path)
    image = cv2.imread(path)
    # print(image)
    res_img = cv2.resize(image, (640, 480))
    cv2.imwrite(Data_root+'/depth_new/'+'depth'+str(num)+'.png', res_img )
    num+=1
print("Done saving images")