import cv2
#import numpy as np
# Load immage as grayscale
img = cv2.imread("Lenna.png", 0)
# Calculate gradient using the sobel operator
grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize =3)
grad_Y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize =3)
# Calculate the gradient magnitude and direction
mag, angle = cv2.cartToPolar(grad_x, grad_Y, angleInDegrees=True)
# Normalize the gradient magnitude to 0-255 range
mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# Display the orginal and gradient image
cv2.imshow("Original", img)
cv2.imshow("Gradient Image", mag)
cv2.waitKey(0)
cv2.destroyAllWindows()
