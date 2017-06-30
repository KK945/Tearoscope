from scipy.cluster.vq import vq, kmeans
from matplotlib import pyplot as plt
import numpy as np
import time as t
from PIL import Image
import cv2

path = 'img/img1.jpg'

orig = cv2.imread(path)
gray = cv2.imread(path,0)

# global thresholding
#ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# Otsu's thresholding

ret2,th2 = cv2.threshold(gray,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering

blur = cv2.GaussianBlur(gray,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# plot all the images and their histograms

#img contains original Image
#Use th3 for initial markdown which is also BLURRED

#np.set_printoptions(threshold='nan')

th3[th3 == 255] = 1

th3 = th3[..., None]

new_image = np.multiply(th3,orig)


cv2.imshow("New Image",new_image)
cv2.imshow("Actual Image",orig)

cv2.waitKey(0)
cv2.destroyAllWindows()


img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

histimg = cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure(1)
plt.plot(histimg);
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()