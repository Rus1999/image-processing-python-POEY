# for create canvas
import numpy
import cv2

# numpy.zeros(height, width, channel),
canvas = numpy.zeros((500, 500, 3), dtype='uint8')

# (x, y)
start_point = (250, 20)
end_point = (250, 150)
# (BGR)
color = (56, 195, 245)
# thickness (px)
thickness = 7

draw_canvas = cv2.line(canvas, start_point, end_point, color, thickness)
draw_canvas = cv2.line(draw_canvas, (20, 300), (230, 300), color, thickness)
draw_canvas = cv2.line(draw_canvas, (270, 300), (480, 300), color, thickness)
draw_canvas = cv2.line(draw_canvas, (150, 340), (350, 340), color, thickness)
draw_canvas = cv2.line(draw_canvas, (155, 355), (345, 355), color, thickness)

# arrow
arrow_start_point = (20, 20)
arrow_end_point = (200, 50)
arrow_color = (78, 71, 255)
tip_length = 1

draw_canvas = cv2.arrowedLine(draw_canvas, arrow_start_point, arrow_end_point, arrow_color, thickness, tipLength=0.1)
draw_canvas = cv2.arrowedLine(draw_canvas, (480, 20), (300, 50), arrow_color, thickness, tipLength=0.1)

# circle
circle_coordinates = (110, 80)
circle_radius = 30
circle_color = (255, 255, 255)
circle_thickness = -1

draw_canvas = cv2.circle(canvas, circle_coordinates, circle_radius, circle_color, circle_thickness)
draw_canvas = cv2.circle(canvas, (390, 80), circle_radius, circle_color, circle_thickness)
draw_canvas = cv2.circle(draw_canvas, (110, 90), 10, (0, 0, 0), circle_thickness)
draw_canvas = cv2.circle(draw_canvas, (385, 90), 10, (0, 0, 0), circle_thickness)

# ellipse
ellipse_centerCoordinates = (100, 80)
ellipse_axesLength = (70, 30)
ellipse_angle = 0
ellipse_startAngle = 0
ellipse_endAngle = 360
ellipse_color = (3, 144, 252)
ellipse_thickness = 1

draw_canvas = cv2.ellipse(canvas, ellipse_centerCoordinates, ellipse_axesLength, ellipse_angle, ellipse_startAngle, ellipse_endAngle, ellipse_color, ellipse_thickness)
draw_canvas = cv2.ellipse(canvas, (400, 80), (70, 30), 0, 0, 360, ellipse_color, ellipse_thickness)

# rectangle
rectangle_startPoint = (200, 400)
rectangle_endPoint = (300, 450)

draw_canvas = cv2.rectangle(canvas, rectangle_startPoint, rectangle_endPoint, color, thickness-8)



# triangle
p1 = (250, 150)
p2 = (200, 220)
p3 = (300, 220)

cv2.line(canvas, p1, p2, color, 7)
cv2.line(canvas, p2, p3, color, 7)
cv2.line(canvas, p1, p3, color, 7)

cv2.imshow("WOWZAA!!!!", draw_canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
