import cv2
# Load the image
img = cv2.imread('4.png')
# Convert the image from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Enhance the color of the image
enhanced  = cv2.detailEnhance(img, sigma_s=50, sigma_r= 0.15)
cv2.imwrite('savedImage4.jpg', img)
# Display the original and enhanced images
cv2.imshow('Original Image', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
cv2.imshow('Enhanced Image',enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()