import argparse
import numpy as np
import cv2

def mse(imageA, imageB):
    prediction = cv2.imread(imageA,0)
    actual = cv2.imread(imageB,0)
    
    err = np.sum((prediction.astype("float") - actual.astype("float")) ** 2)
    err /= float(prediction.shape[0] * prediction.shape[1])
    print("RMSE = ", err)
    
    cv2.imshow('prediction',prediction)
    cv2.imshow('actual',actual)

    cv2.waitKey(10000)
    cv2.destroyAllWindows()
    
    return err




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Simple testing funtion for Monodepthv2 models.')

    parser.add_argument('--imageA', type=str,
                        help='path to a test image or folder of images', required=True)
    parser.add_argument('--imageB', type=str,
                        help='path to a test image or folder of images', required=True)                    
    
    args = parser.parse_args()
    val = mse(args.imageA,args.imageB)
    # print(val)
