# Experiment no:12
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('inp3.tif')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
cv2.imshow("Original", img)
cv2.imshow("2D Filter Averaging", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()