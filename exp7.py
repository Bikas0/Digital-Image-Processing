import cv2
import numpy as np

# Load input image
img = cv2.imread('Lenna.png')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding to the image
thresh_val = 128
max_val = 255
thresh_type = cv2.THRESH_BINARY
_, binary_img = cv2.threshold(gray_img, thresh_val, max_val, thresh_type)
# Display the original and segmented images
cv2.imshow("Original Image", img)
cv2.imshow("Segmented Image", binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
