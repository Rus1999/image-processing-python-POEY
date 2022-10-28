import cv2
import numpy as np

ogImg = cv2.imread("R://workspace//image-processing-python-POEY//week16//images//textbwnoise1.jpg", 0)

kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(ogImg, cv2.MORPH_OPEN, kernel)

cv2.imshow("OG", ogImg)
cv2.imshow("Opening", opening)
cv2.imwrite("R://workspace//image-processing-python-POEY//week16//images//opening.png", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
