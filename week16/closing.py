import cv2
import numpy as np

ogImg = cv2.imread("R://workspace//image-processing-python-POEY//week16//images//textbwnoise2.jpg", 0)

kernel = np.ones((7, 7), np.uint8)

closing = cv2.morphologyEx(ogImg, cv2.MORPH_CLOSE, kernel)
closing = cv2.dilate(closing, (3, 3), iterations=1)

cv2.imshow("OG", ogImg)
cv2.imshow("Closing", closing)
cv2.imwrite("R://workspace//image-processing-python-POEY//week16//images//closeing.png", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
