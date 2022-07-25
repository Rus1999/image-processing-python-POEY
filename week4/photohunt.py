import cv2
import os

# read image
img = cv2.imread("D:\\workspace\\python\\week4\\img\\animal7m.jpg")
'''
# print shape
print(img.shape)

# draw

draw_img = cv2.circle(img, (768, 30), 20, (255, 0, 0), 2)
draw_img = cv2.circle(img, (662, 150), 30, (255, 0, 0), 2)
draw_img = cv2.circle(img, (843, 145), 15, (255, 0, 0), 2)
draw_img = cv2.circle(img, (905, 52), 20, (255, 0, 0), 2)
draw_img = cv2.ellipse(img, (600, 250), (45, 20), 0, 0, 360, (255, 0, 0), 2)
draw_img = cv2.circle(img, (768, 380), 50, (255, 0, 0), 2)
draw_img = cv2.ellipse(img, (666, 395), (45, 20), 90, 0, 360, (255, 0, 0), 2)

# show image
'''
cv2.imshow("Photo hunt", img)
'''
# save file
os.chdir("D:\\workspace\\python\\week4\\img\\")
cv2.imwrite("circled.jpg", draw_img)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()
