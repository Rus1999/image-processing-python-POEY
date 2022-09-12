import cv2
import numpy

og = cv2.imread("D://workspace//python//week11//pic-20220905//7.JPG")

result = numpy.array(255*(og/255)**0.6, dtype="uint8")

cv2.imshow("og", og)
cv2.imshow("WOW ZAA!!!", result)

cv2.imwrite("D://workspace//python//week11//pic-20220905//7fix.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()