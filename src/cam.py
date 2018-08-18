import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("OpenCV Python Implementation")
count = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("OpenCV Python Implementation", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        print("Closing...")
        break
    elif k%256 == 32:
        name = "Captures/pythoncv.jpg".format(count)
        cv2.imwrite(name, frame)
        print("Saved Successfully".format(name))
        count += 1

cam.release()
cv2.destroyAllWindows()
