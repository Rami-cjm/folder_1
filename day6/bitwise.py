#사진의 hsv를 조절하는 코드
import cv2
import numpy as np

def callBack(value):
    pass

path = 'cat.jpg'

image = cv2.imread(path)
 
# img1 = np.zeros((300,300), dtype ='uint8')
# img2 = np.zeros((300,300), dtype ='uint8')


# cv2.rectangle(img1, (25,25), (275, 275), 255, -1)
# cv2.circle(img2, (150,150),150, 255, -1)


cv2.namedWindow("Slider", cv2.WINDOW_NORMAL)
cv2.createTrackbar("low_h", "Slider", 0, 179, callBack)
cv2.createTrackbar("low_s", "Slider", 0, 255, callBack)
cv2.createTrackbar("low_v", "Slider", 0, 255, callBack)
cv2.createTrackbar("high_h", "Slider", 179, 179, callBack)
cv2.createTrackbar("high_s", "Slider", 255, 255, callBack)
cv2.createTrackbar("high_v", "Slider", 255, 255, callBack)

img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#위의 네모 이미지랑 원 이미지 합치는 과정
# b_and = cv2.bitwise_not(img1, img2)
# b_and = cv2.bitwise_and(img1, img2)

# cv2.imshow("Rectangle", img1)
# cv2.imshow("Circle", img2)
#cv2.imshow('And', b_and)

while True:
    low_h = cv2.getTrackbarPos("low_h", "Slider")
    low_s = cv2.getTrackbarPos("low_s", "Slider")
    low_v = cv2.getTrackbarPos("low_v", "Slider")

    high_h = cv2.getTrackbarPos("high_h", "Slider")
    high_s = cv2.getTrackbarPos("high_s", "Slider")
    high_v = cv2.getTrackbarPos("high_v", "Slider")

    low = np.array([low_h, low_s, low_v])
    high = np.array([high_h, high_s, high_v])
    print(low, high)

    mask = cv2.inRange(img_hsv, low, high)
    result = cv2.bitwise_and(img_hsv, img_hsv, mask=mask)


    cv2.imshow('Original image', image)
    cv2.imshow('Color Detector', result)


    if cv2.waitKey(10) & 0xff == 27:
        break

cv2.destroyAllWindows() 

