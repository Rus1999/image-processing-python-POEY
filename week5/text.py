import cv2
import numpy
import os

# canvas height x width
canvas = numpy.zeros((500, 750, 3), dtype='uint8')

# x, y
coordinate = (10, 480)
font = cv2.FONT_HERSHEY_DUPLEX
fontScale = 1
color = (82, 59, 255)
thickness = 2

# grass
canvasDraw = cv2.rectangle(canvas, (0, 300), (750, 500), (69, 138, 70), -1)

# mountain
canvasDraw = cv2.ellipse(canvasDraw, (250, 300), (300, 100), 0, 180, 360, (36, 36, 56), -1)
canvasDraw = cv2.ellipse(canvasDraw, (0, 300), (300, 100), 0, 180, 360, (77, 77, 111), -1)
canvasDraw = cv2.ellipse(canvasDraw, (500, 300), (300, 120), 0, 180, 360, (54, 54, 77), -1)


# right side
canvasDraw = cv2.line(canvasDraw, (300, 300), (750, 500), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (310, 300), (750, 480), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (320, 300), (750, 460), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (330, 300), (750, 440), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (340, 300), (750, 420), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (350, 300), (750, 400), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (360, 300), (750, 380), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (370, 300), (750, 360), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (380, 300), (750, 340), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (390, 300), (750, 320), (12, 69, 10))

# left side
canvasDraw = cv2.line(canvasDraw, (290, 300), (0, 500), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (280, 300), (0, 450), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (270, 300), (0, 425), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (260, 300), (0, 400), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (250, 300), (0, 375), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (240, 300), (0, 350), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (230, 300), (0, 325), (12, 69, 10))
canvasDraw = cv2.line(canvasDraw, (220, 300), (0, 300), (12, 69, 10))

# moon
canvasDraw = cv2.circle(canvasDraw, (100, 70), 30, (224, 254, 255), -1)

# star
canvasDraw = cv2.circle(canvasDraw, (50, 70), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (0, 10), 2, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (25, 90), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (350, 40), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (400, 50), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (500, 30), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (600, 20), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (100, 25), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (750, 15), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (450, 10), 1, (224, 254, 255), -1)

canvasDraw = cv2.circle(canvasDraw, (750, 10), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (470, 100), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (690, 80), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (630, 90), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (590, 70), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (740, 60), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (700, 50), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (430, 40), 1, (224, 254, 255), -1)
canvasDraw = cv2.circle(canvasDraw, (680, 30), 1, (224, 254, 255), -1)

# fence
canvasDraw = cv2.rectangle(canvasDraw, (710, 310), (735, 500), (40, 40, 40), -1)
canvasDraw = cv2.rectangle(canvasDraw, (600, 300), (623, 450), (40, 40, 40), -1)
canvasDraw = cv2.rectangle(canvasDraw, (500, 290), (520, 405), (40, 40, 40), -1)
canvasDraw = cv2.rectangle(canvasDraw, (420, 285), (435, 365), (40, 40, 40), -1)
canvasDraw = cv2.rectangle(canvasDraw, (375, 282), (385, 342), (40, 40, 40), -1)
canvasDraw = cv2.rectangle(canvasDraw, (350, 280), (355, 330), (40, 40, 40), -1)
canvasDraw = cv2.rectangle(canvasDraw, (325, 278), (330, 318), (40, 40, 40), -1)
canvasDraw = cv2.rectangle(canvasDraw, (305, 275), (307, 305), (40, 40, 40), -1)

# name
canvasDraw = cv2.putText(canvasDraw, 'Rus07', coordinate, font, fontScale, (0, 0, 0), thickness+2)
canvasDraw = cv2.putText(canvasDraw, 'Rus07', coordinate, font, fontScale, color, thickness)

canvasDraw = cv2.circle(canvasDraw, (50,50), 40, (0,0,255), -1)
canvasDraw = cv2.circle(canvasDraw, (50,50), 20, (255,0,0), 3)

cv2.imshow("WoW Zaa!!!", canvasDraw)

os.chdir("D:\\workspace\\python\\week5\\img\\")
cv2.imwrite("circled.jpg", canvasDraw)

cv2.waitKey(0)
cv2.destroyAllWindows()
