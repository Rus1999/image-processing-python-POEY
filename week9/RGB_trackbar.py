import cv2
import numpy


def nothing(x):
    pass


# window
img = numpy.zeros((512, 512, 3), numpy.uint8)
cv2.namedWindow("WOW ZAA!!!", cv2.WINDOW_NORMAL)

# color trackbar
cv2.createTrackbar("R", "WOW ZAA!!!", 0, 255, nothing)
cv2.createTrackbar("G", "WOW ZAA!!!", 0, 255, nothing)
cv2.createTrackbar("B", "WOW ZAA!!!", 0, 255, nothing)

while True:
    cv2.imshow("WOW ZAA!!!", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    r = cv2.getTrackbarPos("R", "WOW ZAA!!!")
    g = cv2.getTrackbarPos("G", "WOW ZAA!!!")
    b = cv2.getTrackbarPos("B", "WOW ZAA!!!")

    img[:] = [b, g, r]

cv2.destroyAllWindows()
