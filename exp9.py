
# Experiment no: 09
import numpy as np
import cv2
path = 'itsohk.png'
image = cv2.imread(path, -1)
# Preprocessing the Image
img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
twoDimage = img.reshape((-1,3))
twoDimage = np.float32(twoDimage)
# Defining Parameters
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
attempts=10
# Apply K-Means
ret,label,center=cv2.kmeans(twoDimage,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
result_image = res.reshape((img.shape))
#combined_img = cv2.hconcat([image, result_image])
# Image Show
cv2.imshow("Orginal Image", image)
cv2.imshow('Segmented image', result_image)
#cv2.imshow('Segmenteds image', combined_img)
cv2.waitKey(0)
# closing all open windows
cv2.destroyAllWindows()
