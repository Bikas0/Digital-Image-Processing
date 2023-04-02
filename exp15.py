# https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
# Experiment no: 15
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('inp1.tif')
img = cv2.resize(img, (420,420))
blur = cv2.GaussianBlur(img,(5,5),0)

#image show
cv2.imshow("Orginal Image", img)
cv2.imshow("Gaussian filter image", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()