import cv2
import os

cap = cv2.VideoCapture("D:\\workspace\\python\\video\\In the end, there is light in the darkness (480p_24fps_H264-128kbit_AAC).mp4")

# create a folder
try:
    if not os.path.exists("D:\\workspace\\python\\mkvideo\\"):
        os.makedirs("D:\\workspace\\python\\mkvideo\\")
except OSError:
    print("Error: creating folder")

if cap.isOpened() == False:
    print("Error opening video file")

currentframe = 0

while cap.isOpened():
    # capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        # convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # save frame
        name = "D:\\workspace\\python\\mkvideo\\frame"+str(currentframe)+".jpg"
        cv2.imwrite(name, gray)

        cv2.imshow("Result", gray)

        currentframe += 1
        # exit by q
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

'''
# capture frame by frame
ret, frame = cap.read()
if ret == True:
    cv2.imshow("Result", frame)
    # exit by q
cv2.waitKey(0)
'''

cap.release()
cv2.destroyAllWindows()
