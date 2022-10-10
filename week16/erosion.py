import cv2
import numpy as np

ogImg = cv2.imread("R://workspace//image-processing-python-POEY//week16//images//textbw.jpg", 0)

kernel = np.ones((7, 7), np.uint8)

erosion = cv2.erode(ogImg, kernel, iterations=1)

cv2.imshow("OG", ogImg)
cv2.imshow("erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()