import cv2
import numpy as np

ogImg = cv2.imread("R://workspace//image-processing-python-POEY//week16//images//textbw.jpg", 0)

kernel = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(ogImg, kernel, iterations=1)

cv2.imshow("OG", ogImg)
cv2.imshow("Dilation", dilation)
cv2.imwrite("R://workspace//image-processing-python-POEY//week16//images//dilation.png", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
