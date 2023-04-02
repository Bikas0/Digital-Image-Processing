import cv2 
import numpy as np 
img = cv2.imread("3.jfif")
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
b, g,r = cv2.split(img)
m = img.shape[0]
n = img.shape[1]
matrix = np.ones((m,n), dtype="uint8")
# increase the intensity of each color channel
b = cv2.add(b, matrix*50)
g = cv2.add(g, matrix*50)
r = cv2.add(r, matrix*50)
brightened_img = cv2.merge([b, g, r])
cv2.imshow("Orginal", img)
cv2.imshow("Brightened Image", brightened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()