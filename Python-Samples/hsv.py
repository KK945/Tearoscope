import cv2
from scipy.cluster.vq import vq, kmeans
from matplotlib import pyplot as plt
import numpy as np
import time as t
from PIL import Image

path = 'img/img1.jpg'


img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

histimg = cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure(1)
plt.plot(histimg);
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


#hist = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.hist(img.ravel(),256,[0,256]); 
#plt.show()