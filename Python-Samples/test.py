from sklearn.cluster import KMeans
import numpy as np
import cv2



image = cv2.imread("img/img1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
# Resize it
h, w, _ = image.shape
w_new = int(400 * w / max(w, h) )
h_new = int(400 * h / max(w, h) )
 
image = cv2.resize(image, (w_new, h_new));


# Reshape the image to be a list of pixels
image_array = image.reshape((image.shape[0] * image.shape[1], 3))

# Clusters the pixels
clt = KMeans(n_clusters = 3)
clt.fit(image_array)


cv2.imshow('image',image)
cv2.waitKey(0);
cv2.destroyAllWindows()
