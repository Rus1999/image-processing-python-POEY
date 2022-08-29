import cv2
import numpy

canvas = numpy.zeros((100, 100, 3), dtype='uint8')


# draw_canvas = cv2.ellipse(canvas, (50, 70), (40, 10), 0, 0, 360, (0, 0, 225), -1)
# draw_canvas = cv2.ellipse(canvas, (50, 40), (10, 40), 50, 1, 360, (0, 0, 255), -1)
draw_canvas = cv2.line(canvas, (30, 90), (60, 10), (0, 0, 225), 5)

cv2.imshow("a", draw_canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()