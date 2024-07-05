#강사님이 작성하신거 복붙함 
import cv2
import numpy as np

path1 = 'cat.jpg'
path2 = 'dog.jpg'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
# print(img1.shape)
print(img2.shape)
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
print(img1.shape)
img3 = cv2.add(img1, img2)

mask = np.ones((img2.shape[0], img2.shape[1], 3), dtype='uint8') * 50
print(mask.shape)
img1_b = cv2.add(img1, mask) 
img2_d = cv2.subtract(img2, mask)
'''
cv2.imshow("Cat", img1) 
cv2.imshow("Cat_b", img1_b)
cv2.imshow("Dog", img2)
cv2.imshow("Dog_d", img2_d)
cv2.imshow("Dog + Cat", img3)
'''
#roi는 이미지를 슬라이싱 하는 작업
#cv2.imshow("Cat", img1[:100,:,:])



img_green = img1
img_green[0:img1.shape[0]//2, :, :] = [0,255,0]

#사진에서 
#img1[:,:, 0] = 0
#img1[:,:, 1] = 255
#img1[:,:, 2] = 0

cv2.imshow("roi", img_green)
#cv2.imshow("Cat", img1)
cv2.waitKey()
cv2.destroyAllWindows()

