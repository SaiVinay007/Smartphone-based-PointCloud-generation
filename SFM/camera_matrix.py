import cv2
import numpy as np


def get_essential_matrix(K, F):
    # 3x3
    E = np.matmul(np.matmul(K.transpose(), F), K)
    return E


def get_fundamental_matrix(kpt_locs1, kpt_locs2):
    # 3x3
    kpt_locs1 = np.asarray(kpt_locs1)
    kpt_locs2 = np.asarray(kpt_locs2)

    F, mask = cv2.findFundamentalMat(kpt_locs1, kpt_locs2, cv2.FM_RANSAC, 0.1, 0.99 )
    
    return F


def get_calibration_matrix():

    # we get this from the camera properties intrinsic matrix
    # Use self calibration if intrinsic matrix not available (single-view metrology constraints, 
    # the direct approach using the Kruppa equations, the algebraic approach or the stratified approach)
    K = None
    return K


def get_camera_matrix(E):

    u, s, vt = np.linalg.svd(E)
    W = np.array([[0, -1, 0],
                  [1, 0, 0],
                  [0, 0, 1]])
    R =  np.matmul(np.matmul(u, W), vt)
    t = u[2]

    # first camera matrix P1 is assumed at origin - no rotation or translation
    P1 = np.array([[0,0,0,0], 
                    [0,0,0,0], 
                    [0,0,0,0]])
    P2 = np.concatenate((R, np.expand_dims(t, axis=1)), axis=1)

    return P1, P2


def align_matched_points(keypoints, matches):

    kpt_locs1 = []
    kpt_locs2 = []

    for i in range(len(matches)):
        
        # queryIdx is the "left" image and trainIdx is the "right" image
        # kpt_locs1 has [x,y] of left image and kpt_locs2 has the right image's
        kpt_locs1.append(keypoints[0][matches[i][0].queryIdx].pt)
        kpt_locs2.append(keypoints[1][matches[i][0].trainIdx].pt)

    return kpt_locs1, kpt_locs2


if __name__=='__main__':

    # calculated in point_matching.py 
    keypoints = None
    matches = None
    
    
    kpt_locs1, kpt_locs2 = align_matched_points(keypoints, matches)