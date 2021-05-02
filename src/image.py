import cv2 as cv

def readImage(path):
    return  cv.imread(path,0)

def writeImage(img, name):
    cv.imwrite(name, img)

def cropImageHorizontal(img, start, end):
    return img[start:end, :]

def cropImageVertical(img, start, end):
    return img[:, start:end]