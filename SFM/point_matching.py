import cv2
import os
import matplotlib.pyplot as plt
import numpy as np


def get_featuredescriptors(image):

    surf = cv2.xfeatures2d.SURF_create()
    # surf = cv2.SURF(400)
    kp, des = surf.detectAndCompute(image,None)

    return kp, des


def feature_matching(des1, des2, percent=100):

    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params,search_params)

    matches = flann.knnMatch(des1,des2,k=2)
    
    # The percentage of matches that you want to retain
    num = len(matches)//(100//percent)
    matches = matches[:num]

    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in range(len(matches))]

    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            matchesMask[i]=[1,0]

    draw_params = dict(matchColor = (0,255,0),
                    singlePointColor = (255,0,0),
                    matchesMask = matchesMask,
                    flags = 0)

    return matches, draw_params


def pixel_locations(image1, image2, i, total_imgs):

    # img1 = cv2.imread('./images/'+image1)
    img1 = cv2.imread('./images/'+'0000.ppm')
    img2 = cv2.imread('./images/'+image2)

    # print(img1, img2, total_imgs, image1, image2)

    feat1, desps1 = get_featuredescriptors(img1)
    feat2, desps2 = get_featuredescriptors(img2)

    keypoints.append(feat1)
    keypoints.append(feat2)

    descriptors.append(desps1)
    descriptors.append(desps2)

    matches, draw_params = feature_matching(descriptors[0], descriptors[1])

    i = -1
    x = []
    y = []
    while(True):
        i+=1

        if i>len(matches):
            break
        try:
            x.append(keypoints[0][matches[i][1].trainIdx].pt[0])
            y.append(keypoints[0][matches[i][1].trainIdx].pt[1])
        except Exception:
            pass

    # If you want to visualize matched points
    # img = cv2.drawMatchesKnn(images[0], keypoints[0], images[1], keypoints[1], matches, None, **draw_params)


    return x, y




if __name__=='__main__':


    images_paths = os.listdir("./images")
    total_imgs = len(images_paths)

    images = []
    keypoints = []
    descriptors = [] 

    x_vals = []
    y_vals = []
    
    for i in range(total_imgs-1):

        image1 = images_paths[i%total_imgs]
        image2 = images_paths[(i+1)%total_imgs]

        x, y = pixel_locations(image1, image2, i, total_imgs)
        # print(len(x), len(y))
        x_vals.extend(x)
        y_vals.extend(y)

    

    # for i in images_paths:

    #     img = cv2.imread('./images/'+i)
        
    #     images.append(img)
    #     feat, desps = get_featuredescriptors(img)
        
    #     keypoints.append(feat)
    #     descriptors.append(desps)


    # matches, draw_params = feature_matching(descriptors[0], descriptors[1])

    # i = -1
    # x = []
    # y = []
    # while(True):
    #     i+=1

    #     if i>len(matches):
    #         break
    #     try:
    #         x.append(keypoints[0][matches[i][1].trainIdx].pt[0])
    #         y.append(keypoints[0][matches[i][1].trainIdx].pt[1])
    #     except Exception:
    #         pass
        

    


    x = np.array(x_vals)
    y = np.array(y_vals)
    print(x.shape, y.shape)

    # y = np.random.rand(N)
    colors = (0,0,0)
    area = np.pi*3

    # Plot
    plt.figure(figsize=(20,10))
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.title('Scatter plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


    # plt.imshow(img,)
    # plt.show()

    # cv2.imshow('image',image1)
    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()