import cv2 as cv
import numpy as np

def readImage(path):
    return  cv.imread(path,0)

def writeImage(img, name):
    cv.imwrite(name, img)

def cropImageHorizontal(img, start, end):
    return img[start:end, :]

def cropImageVertical(img, start, end):
    return img[:, start:end]
    
def getHorizontalHistogram(img):
    return img.shape[1] - np.sum(img,axis=1,keepdims=True)/255

def getVerticalHistogram(img):
    return img.shape[0] - np.sum(img,axis=0,keepdims=True)/255