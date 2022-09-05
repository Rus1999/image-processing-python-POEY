import cv2

img = cv2.imread("D:\\workspace\\python\\week11\\pic-20220905\\rocklee.jpg", 1)

output_neg = 255 - img

cv2.imshow("WOW ZAA!!! OG", img)
cv2.imshow("WOW ZAA!!!", output_neg)
cv2.waitKey(0)
cv2.destroyAllWindows()
