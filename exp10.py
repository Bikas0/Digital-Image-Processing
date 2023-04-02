# load the required packages
import cv2
import numpy as np
# load the image into system memory
image = cv2.imread('sharp.png', flags=cv2.IMREAD_COLOR)
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

cv2.imshow("Orginal Image", image)
cv2.imshow('Sharpened Image', image_sharp)
cv2.waitKey()
cv2.destroyAllWindows()