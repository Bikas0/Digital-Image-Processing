# import the required library
import cv2
# read the input image
image = cv2.imread('b.jpg')
# define the alpha and beta
alpha = 2.5 # Contrast control
beta = 0 # Brightness control
# call convertScaleAbs function
adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta = beta)
# display the output image
cv2.imshow("Orginal", image)
cv2.imshow('Contrast Image', adjusted)
cv2.waitKey()
cv2.destroyAllWindows()