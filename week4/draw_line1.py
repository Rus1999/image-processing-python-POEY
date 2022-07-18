# for create canvas
import numpy
import cv2

# numpy.zeros(height, width, channel),
canvas = numpy.zeros((400, 500, 3), dtype='uint8')

# (x, y)
start_point = (250, 20)
end_point = (250, 200)
# (BGR)
color = (56, 195, 245)
# thickness (px)
thickness = 7

draw_canvas = cv2.line(canvas, start_point, end_point, color, thickness)
draw_canvas = cv2.line(draw_canvas, (20, 300), (230, 300), color, thickness)
draw_canvas = cv2.line(draw_canvas, (270, 300), (480, 300), color, thickness)
draw_canvas = cv2.line(draw_canvas, (70, 70), (70, 70), color, 20)
draw_canvas = cv2.line(draw_canvas, (430, 70), (430, 70), color, 20)
draw_canvas = cv2.line(draw_canvas, (150, 320), (350, 320), color, thickness)
draw_canvas = cv2.line(draw_canvas, (155, 335), (345, 335), color, thickness)

cv2.imshow("Result", draw_canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
