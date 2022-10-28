import cv2
import numpy

img = cv2.imread("R:/workspace/image-processing-python-POEY/week11//pic-20220905//goku.png", 1)

# img_log = (numpy.log(img+1)/(numpy.log(1.0+numpy.max(img))))*255
c = 255/(numpy.log(1.0+numpy.max(img)))
img_log = c * numpy.log(1.0 + img)
img_log = numpy.array(img_log, dtype=numpy.uint8)

cv2.imshow("OG", img)
cv2.imshow("WOW ZAA!!!", img_log)
cv2.waitKey(0)
cv2.destroyAllWindows()
