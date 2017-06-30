import cv2
from scipy.cluster.vq import vq, kmeans
from matplotlib import pyplot as plt
import numpy as np
import time as t
from PIL import Image

path = 'img/img1.jpg'


img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print img[101][2][2]

#hist = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.hist(img.ravel(),256,[0,256]); 
#plt.show()