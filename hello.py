import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 200)
cap.set(4, 100)
low = 50
high = 150


#callback은 무슨 의미...?
def callback(value):
    pass

# cv2.namedWindow("On Air", cv2.WINDOW_NORMAL)

# cv2.createTrackbar("high_t", "On Air", 1, 20, callback)
# cv2.createTrackbar("high_B", "On Air", 1, 255, callback)
# cv2.createTrackbar("high_G", "On Air", 1, 255, callback)
# cv2.createTrackbar("high_R", "On Air", 1, 255, callback)

while True:    
    _, frame =cap.read()   
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame = cv2.flip(frame, 1)


    # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert의 cvt bgr 
    # canny_frame = cv2.Canny(gray_frame, low, high ) #gray컬러 
    # blur_frame = cv2.GaussianBlur(frame, (11,11), 10) #blur 처리 # 끝에 0은 표준편차를 말함 가운데 7,7은 홀수만 가능
    # high_t = cv2.getTrackbarPos("high_t", "On Air")
    #이건 한섭이가 한 거 
    # frame[:,:,0] = frmae[:,:,0]+ cv2.getTrackbarPos("high_B", "On Air")
    # frame[:,:,0] = frmae[:,:,0]+ cv2.getTrackbarPos("high_G", "On Air")
    # frame[:,:,0] = frmae[:,:,0]+ cv2.getTrackbarPos("high_R", "On Air")

    # hsv_frame = cv2.getTrackbarPos("HSV", "On Air")

    #이건 내가 한 거 
    # high_B = cv2.getTrackbarPos("high_B", "On Air")
    # high_G = cv2.getTrackbarPos("high_G", "On Air")
    # high_R = cv2.getTrackbarPos("high_R", "On Air")


    cv2.imshow("HSV", hsv_frame)
    cv2.imshow("Original", frame)
    # cv2.imshow("On Air", hsv_frame)

    #cv2.imshow("Gray", gray_frame)
    #cv2.imshow("Canny", canny_frame) #이건 마치 스케치한 것 처럼 보여주는 거 
    #cv2.imshow("Blur", blur_frame) #카메라 기능 중에 블러 처리 같은 너낌 
 


 

    if cv2.waitKey(10) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


