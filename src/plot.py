import numpy as np
from matplotlib import pyplot as plt

def plotImage(img, title="Imagem"):
    plt.imshow(img,'gray')
    plt.title(title)
    plt.xticks([]),plt.yticks([])
    plt.show()

def plotHistogram(array, title="histogram"):
    plt.plot(array)
    plt.show()