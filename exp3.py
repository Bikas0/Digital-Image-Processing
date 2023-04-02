# Experiment no: 03
import cv2
# Load the image in color mode
img = cv2.imread("Lenna.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Invert the color image
neg_img = 255 - img
neg_gray_img = 255 - gray
# Display the original and negative images side by side
combined_img = cv2.hconcat([img, neg_img])
combined_gray_img = cv2.hconcat([gray, neg_gray_img])
cv2.imshow("Original RGB vs Negative Image", combined_img)
cv2.imshow("Gray vs orginal Image", combined_gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
