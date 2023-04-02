import cv2

# Read the image
img = cv2.imread("image.jpg")

# Convert the image to LAB color space
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Split the LAB image into its channels
l, a, b = cv2.split(lab)

# Apply histogram equalization to the A and B channels
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
a = clahe.apply(a)
b = clahe.apply(b)

# Merge the LAB channels back together
lab = cv2.merge((l, a, b))

# Convert the image back to the BGR color space
result = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

# Display the original and result images
cv2.imshow("Original", img)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
