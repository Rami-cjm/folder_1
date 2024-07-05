import cv2
import numpy as np

img_path = 'bear.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img, (400,400))


def callback1(value):
    pass
def callback2(value):
    pass

cv2.namedWindow("Style", cv2.WINDOW_NORMAL)
cv2.createTrackbar("Sigma_S", "Style", 0, 200, callback1)
cv2.createTrackbar("Sigma_R", "Style", 0, 10, callback2)

while True:
    sigma_S = cv2.getTrackbarPos("Sigma_S", "Style")
    sigma_R = cv2.getTrackbarPos("Sigma_R", "Style") / 10.0

    img_style = cv2.stylization(img, sigma_s = sigma_S, sigma_r = sigma_R) #sigmas는 해상도 sigma r은 만화처럼 그려지는 화면에서 선 조절? 

    cv2.imshow("Image", img)
    cv2.imshow('Style', img_style)

    if cv2.waitKey(10) & 0xff == ord('q'): #key 입력할 때 소문자로 입력하면 실행이 안 되니 주의하자
        break

cv2.destroyAllWindows()
