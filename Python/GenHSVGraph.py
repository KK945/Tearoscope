"""
=============================================
DESQ (Dry Eyes Syndrome Quantifier)
=============================================
AUTHOR: Om Prakash S
Date: 30-06-2017
Engineering the Eye 5
SRUJANA Center for Innovation
---------------------------------------------
Python Code to Generate Hue Graph of colors 
formed in the Lipid Layer surface.
----------------------------------------------
The resultant Image is Graph containing Hue 
plottings.
----------------------------------------------
"""

from scipy.cluster.vq import vq, kmeans
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import time as t
import cv2

path = 'img/img1.jpg' #Change Path here

img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

histimg = cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure(1)
plt.plot(histimg);
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

