import cv2
import numpy

img = cv2.imread("D://workspace//python//week11//pic-20220905//goku.png")

img_gamma1 = numpy.array(255*(img/255)**5, dtype="uint8")
img_gamma2 = numpy.array(255*(img/255)**0.5, dtype="uint8")

cv2.imshow("Input", img)
cv2.imshow("Output gamma1", img_gamma1)
cv2.imshow("Output gamma2", img_gamma2)

cv2.waitKey(0)
cv2.destroyAllWindows()