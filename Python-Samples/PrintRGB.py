#Python Program to print RGB Pixel values of a Image
import cv2
import numpy as np
from PIL import Image

img = Image.open('img/img1.jpg') #Image Path here
img = img.convert("RGB")
datas = img.getdata()

for item in datas:
    print item
