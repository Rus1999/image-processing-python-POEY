import cv2
import os

# print("Your OpenCV version is: " + cv2.__version__)

# read an image
img = cv2.imread("D:\\workspace\\python\\picture\\chicken.png", 1)

print(img.shape)

# convert color image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# save file
os.chdir("D:\\workspace\\python\\picture\\")
cv2.imwrite("graypic.jpg", gray)

# show the image
cv2.imshow("Result", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
