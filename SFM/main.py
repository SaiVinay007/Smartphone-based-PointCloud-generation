import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


from point_matching import *
from camera_matrix import *


images_paths = os.listdir("./images")

images = []
keypoints = []
descriptors = [] 

# --------------------------------------------------
# Get the images and ther keypoints, descriptors
for i in images_paths:
    img = cv2.imread('./images/'+i)
    images.append(img)

    kps, desps = get_featuredescriptors(img)
    keypoints.append(kps)
    descriptors.append(desps)


# --------------------------------------------------
# Do matching 
matches, draw_params = feature_matching(descriptors[0], descriptors[1])
# print(features[matches[0].queryIdx].pt)
# print(keypoints[0][matches[50][1].trainIdx].pt)
matched_image = cv2.drawMatchesKnn(images[0], keypoints[0], images[1], keypoints[1], matches, None, **draw_params)
# plt.imshow(matched_image,)
# plt.show()


# --------------------------------------------------
# Aligning the matched points(the matched points location is set 
# to a index as same for both left and right images) into two lists
kpt_locs1, kpt_locs2 = align_matched_points(keypoints, matches)
# print(len(kpt_locs1))


# --------------------------------------------------
# Get the fundamental and essential matrices

F = get_fundamental_matrix(kpt_locs1, kpt_locs2)
K = get_calibration_matrix()
E = get_essential_matrix(K, F)
# E = np.array([[0, -1, 0],
#                   [1, 0, 0],
#                   [0, 0, 1]])

# print(F.shape, K.shape, E.shape)
P1, P2 = get_camera_matrix(E)

# For the dataset they we already have P1 and P2
P1 = np.array([[-828.467, 1102.59, -71.2296, 31390], 
      [-144.854, -8.84907, -1335.41, 22230.2], 
      [-0.947171, -0.255863, -0.193394, 60.9943]]) 


P2 = np.array([[-1104.11, 825.828, -69.2329, 31583.3 ],
               [-141.535 ,-47.0052, -1333.37, 22406.5 ],
               [-0.839833, -0.506883, -0.194292, 60.5264]]) 

