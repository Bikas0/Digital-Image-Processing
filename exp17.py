import cv2

# Load the input image
img = cv2.imread('bilateral.jpg')
img = cv2.resize(img, (520,520))

# Apply bilateral filter to the image
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# Display the original and filtered images
cv2.imshow('Input Image', img)
cv2.imshow('Bilateral Image produced by Bikas', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
