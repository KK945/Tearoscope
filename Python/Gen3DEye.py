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
formed in the Lipid Layer surface and Plot a 3D
Graph.
----------------------------------------------
The resultant Image is Graph containing 3D Image
Sturcture.
----------------------------------------------
"""

import cv2
from scipy.cluster.vq import vq, kmeans
from matplotlib import pyplot as plt
import numpy as np
import time as t
from PIL import Image

path = 'img/img1.jpg' #Path To Image


img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


