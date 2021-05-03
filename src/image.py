import time
import cv2 as cv
import numpy as np

def readImage(path):
    return  cv.imread(path,0)

def writeImage(img, name):
    cv.imwrite(name, img)

def writeImagesList(imgList, path, format):
    for index, img in enumerate(imgList):
        ts = str(time.time())
        writeImage(img, path + "img_" + ts + "_" + str(index) + format)

def cropImageHorizontal(img, start, end):
    return img[start:end, :]

def cropImageVertical(img, start, end):
    return img[:, start:end]
    
def getHorizontalHistogram(img):
    return img.shape[1] - np.sum(img,axis=1,keepdims=True)/255

def getVerticalHistogram(img):
    return img.shape[0] - np.sum(img,axis=0,keepdims=True)/255

def applyGrayscale(img):
    return img

def applyNoiseRemoval(img):
    return cv.GaussianBlur(img,(5,5),0)
