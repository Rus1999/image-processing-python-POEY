import cv2
import numpy


def nothing(x):
    pass


img = numpy.zeros((512, 512, 3), numpy.uint8)
cv2.namedWindow("WOW ZAA!!!", cv2.WINDOW_NORMAL)

cv2.createTrackbar("H", "WOW ZAA!!!", 0, 180, nothing)
cv2.createTrackbar("S", "WOW ZAA!!!", 0, 255, nothing)
cv2.createTrackbar("I", "WOW ZAA!!!", 0, 255, nothing)

while(True):
    cv2.imshow("WOW ZAA!!!", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    r = cv2.getTrackbarPos("H", "WOW ZAA!!!")
    g = cv2.getTrackbarPos("S", "WOW ZAA!!!")
    b = cv2.getTrackbarPos("I", "WOW ZAA!!!")

    img[:] = [r, g, b]
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

cv2.destroyAllWindows()
