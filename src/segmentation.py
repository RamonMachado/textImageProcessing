import time
import numpy as np
import cv2 as cv
from scipy.signal import find_peaks

from image import writeImage, cropImageHorizontal, cropImageVertical, getHorizontalHistogram, getVerticalHistogram 

def adaptiveThreshold(img):
     return cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv.THRESH_BINARY,11,2)

def getLocalMinimas(array):
    return find_peaks(-array)

def getLocalMaximas(array):
    return find_peaks(array)

def horizontalSegmentation(horizontalHistogram, img):
    horizontalLowerPeaks = getLocalMinimas(horizontalHistogram)
    horizontalCutImages = []
    previousPeak = 0
    # cuts the image based on lower horizontal peaks
    for peak in horizontalLowerPeaks[0]:
        if peak - previousPeak < 20: 
            continue
        horizontalCutImages.append(cropImageHorizontal(img, previousPeak, peak))
        previousPeak = peak
    return horizontalCutImages

def verticalSegmentation(histogram, img):
    lowerPeaks = getLocalMinimas(histogram)
    images = []
    previousPeak = 0
    # cuts the image based on lower horizontal peaks
    for peak in lowerPeaks[0]:
        images.append(cropImageVertical(img, previousPeak, peak))
        previousPeak = peak
    return images

def lineLevelSegmentation(binaryImage):
    histogram = getHorizontalHistogram(binaryImage).flatten()
    return horizontalSegmentation(histogram, binaryImage)

def wordLevelSegmentation(binaryImage):
    histogram = getVerticalHistogram(binaryImage).flatten()
    return verticalSegmentation(histogram, binaryImage)