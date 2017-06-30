import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

path='img/img1.jpg' #Path to Captured Image

orig = cv2.imread(path)
img = cv2.imread(path,0)

# global thresholding
#ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# Otsu's thresholding

ret2,th2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering

blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# plot all the images and their histograms

#img contains original Image
#Use th3 for initial markdown which is also BLURRED

#np.set_printoptions(threshold='nan')

th3[th3 == 255] = 1

th3 = th3[..., None]

new_image = np.multiply(th3,orig)

cv2.imwrite('img/result/img1_AP.jpg', new_image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

cv2.imshow("New Image",new_image)
cv2.imshow("Actual Image",orig)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
for i in xrange(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()
"""