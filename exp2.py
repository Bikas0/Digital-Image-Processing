import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load immage as grayscale
img_bgr = cv2.imread("Lenna.png", 1)
#print(img_bgr.shape)
img_bgr = cv2.resize(img_bgr, [360,360])
   
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img_bgr], [i], None, [256], [0, 256])
    plt.plot(histr, color = col, label = col)
    plt.xlim([0, 256])

gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
cv2.imshow("Orginal Image", img_bgr)
cv2.imshow("Grayscale Image", gray)
# Compute histogram
#hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
# Plot histogram
plt.hist(gray.ravel(), 256, [0, 256], color="gray")
plt.title("Histogram")
plt.xlabel("Pixel Values")
plt.ylabel("No. of pixels")
plt.legend()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
