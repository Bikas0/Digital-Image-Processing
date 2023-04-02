import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('inp1.tif')
img = cv2.resize(img, (360,360))
kernel = np.ones((3,3),np.float32)/9
blur = cv2.filter2D(img,-1,kernel)
#blur = cv2.blur(img,(5,5))
#image show
cv2.imshow("Orginal Image", img)
cv2.imshow("Average filter image", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()