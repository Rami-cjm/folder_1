import cv2
import numpy as np




def callback(value):
    pass
cap = cv2.VideoCapture(0)

cv2.namedWindow("On air", cv2.WINDOW_NORMAL)
cv2.createTrackbar("low_h", "On air", 0, 179, callback)
cv2.createTrackbar("low_s", "On air", 0, 255, callback)
cv2.createTrackbar("low_v", "On air", 0, 255, callback)
cv2.createTrackbar("high_h", "On air", 179, 179, callback)
cv2.createTrackbar("high_s", "On air", 255, 255, callback)
cv2.createTrackbar("high_v", "On air", 255, 255, callback)

#cap_hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)


while True:    
    _, frame =cap.read()   
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    


    low_h = cv2.getTrackbarPos("low_h", "On air")
    low_s = cv2.getTrackbarPos("low_s", "On air")
    low_v = cv2.getTrackbarPos("low_v", "On air")

    high_h = cv2.getTrackbarPos("high_h", "On air")
    high_s = cv2.getTrackbarPos("high_s", "On air")
    high_v = cv2.getTrackbarPos("high_v", "On air")

    low = np.array([low_h, low_s, low_v])
    high = np.array([high_h, high_s, high_v])
    


    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.inRange(hsv_frame, low, high)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 1000:
            cv2.drawContours(hsv_frame, [max_contour], -1, (0, 255,0), 2)

    bitwise_and = cv2.bitwise_and(hsv_frame, hsv_frame, mask=mask)

    cv2.imshow("HSV", bitwise_and)


    if cv2.waitKey(10) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
