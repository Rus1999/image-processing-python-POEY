import cv2
import os

img = cv2.imread("D:\\workspace\\python\\week6\\img\\animal1.jpg")

h, w = img.shape[:2]

# print("Height = {} Width = {}".format(h, w))
print("Height: ", h, ", Width: ", w)

# startRow: endRow, starCol: endCol
roi = img[164:234, 56:112]

os.chdir("D:\\workspace\\python\\week6\\img\\")
cv2.imwrite("roi.jpg", roi)
cv2.imshow("WoW Zaa!!", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
