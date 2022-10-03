import cv2
import numpy

ogImg = cv2.imread("R://workspace//image-processing-python-POEY//week15//images//shape.PNG", 1)

ogImgGrey = cv2.cvtColor(ogImg, cv2.COLOR_BGR2GRAY)

corner = cv2.goodFeaturesToTrack(ogImgGrey, 0, 0.005, 30)
corner = numpy.int0(corner)

for i in corner:
    x, y = i.ravel()
    cv2.circle(ogImg, (x, y), 3, (0, 0, 0), -1)

cv2.imwrite("R://workspace//image-processing-python-POEY//week15//images//shapeCornerDetected.png", ogImg)
cv2.imshow("OG", ogImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
