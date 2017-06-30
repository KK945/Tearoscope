# import the necessary packages
#ffmpeg -i vi1.mp4 -vf select='lt(scene\,0.1),showinfo' -f null info.txt
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2