import cv2

img = cv2.imread("D:\\workspace\\python\\week6\\img\\stone.jpeg")

print("Original Dimensions : ", img.shape)

scale_percent = 60
# height, width
height = int(img.shape[0] * scale_percent/100)
width = int(img.shape[1] * scale_percent/100)

# width, height
dim = (width, height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print("Resized Dimensions : ", resized.shape)

cv2.imshow("OG image", img)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
