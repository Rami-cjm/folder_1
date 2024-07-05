import cv2
import numpy as np

def callback(value):
    pass

img_path = 'cat.jpg'

img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (5,5), 1)


cv2.namedWindow("Slider")
cv2.createTrackbar("high_t","Slider", 10, 255, callback) #10은 초기값? 255는 맥시멈 값

while True:
    high_t = cv2.getTrackbarPos("high_t", "Slider") #이름 쓰고 어디에 있는건지 > Pos안에 괄호 내용()
    img_canny = cv2.Canny(img_blur, 10, high_t)

#getTrackbarPos에서 pos는 position의 약자, trackbar에서 high_t의 위치를 canny로 옮겨주기 위한 명령어?라고 이해하면 되려나...

    cv2.imshow("cat", img_blur)
    cv2.imshow("cat", img_canny)


    if cv2.waitKey(10) & 0xff ==ord('q'):
        break
cv2.destroyAllWindows()

