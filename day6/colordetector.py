import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 200)
cap.set(4, 100)
low = 50
high = 150

def callback(value):
    pass


while True:    
    _, frame =cap.read()
    hsv_frame = cv2.cvtcolor(frame, cv2.COLOR_BGR2GRAY)


     if cv2.waitKey(10) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()