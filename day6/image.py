import cv2
import numpy as np

path = "cat.jpg"
image = cv2.imread(path)

print(image.shape)
print(image.shape[0])

#cv2.circle(image,(image.shape[1] //2, image.shape[0] //2), 5, (0,0,255), -1) #사진에서 빨간 원 점이 만들어짐 
#cv2.circle(image, x,y 
cv2.imshow("cat", image)

cv2.waitKey()
cv2.destroyAllWindows()

