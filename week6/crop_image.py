import cv2

img = cv2.imread("D:\\workspace\\python\\week6\\img\\blackRose.jpg")

h, w = img.shape[:2]

# print("Height = {} Width = {}".format(h, w))
print("Height: ", h, ", Width: ", w)

# startRow: endRow, starCol: endCol
roi = img[325:1000, 125:625]

cv2.imshow("WoW Zaa!!", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
