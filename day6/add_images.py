import cv2
import numpy as np

path1 = 'cat.jpg'
path2 = 'dog.jpg'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
#print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (275, 183)) # 사진을 합칠 때 두 사진의 크기를 맞추는 작업, 위 shape 명령에서 출력칸에 이미지의 크기가 나옴 거기서 맞추는거 
print(img1.shape)
#img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0])) #강사님은 이 명령어를 사용했음
mask = np.ones((img2.shape[0], img2.shape[1], 3), dtype='uint8') * 50 
print(mask.shape)
img1_b = cv2.add(img1, mask)
img2_d = cv2.subtract(img2, mask)


print(img1.shape)
img3 = cv2.add(img1,img2) # img1와 img2 합치는 거 


cv2.imshow("cat", img1)
cv2.imshow("dog", img2)
cv2.imshow("mixed", img3) # img1와 img2 합치는 거 
cv2.imshow("cat_b", img1_b)
cv2.imshow("cat_d", img2_d)

cv2.waitKey()
cv2.destroyAllWindows()