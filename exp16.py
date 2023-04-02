import cv2
from matplotlib import pyplot as plt

img = cv2.imread('inp3.tif')

blur = cv2.medianBlur(img, 3)
#image show
cv2.imshow("Orginal Image", img)
cv2.imshow("Median Blurred", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()