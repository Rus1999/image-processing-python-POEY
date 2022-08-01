import cv2
import os

img = cv2.imread("D:\\workspace\\python\\week6\\img\\roi.jpg")

print("Original Dimensions : ", img.shape)

# height, width
height = int(img.shape[0] * 2.99)
width = int(img.shape[1] * 3)

# width, height
dim = (width, height)
resized = cv2.resize(img, dim)

print("Resized Dimensions : ", resized.shape)

os.chdir("D:\\workspace\\python\\week6\\img")
cv2.imwrite("resized.jpg", resized)
cv2.imshow("OG image", img)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
