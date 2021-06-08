import cv2
import numpy as np

photo=cv2.imread('wm.jpg')
photo1=cv2.imread('bts-pic1.jpg')

cv2.imshow('title',photo)
cv2.imshow('title1',photo1)
cv2.waitKey()    
cv2.destroyAllWindows()


#to paste an image inside another
x=50
y=70
x_end=x+photo.shape[1]
y_end=y+photo.shape[0]
photo1[y:y_end,x:x_end]=photo

cv2.imshow('title1',photo1)
cv2.waitKey()    
cv2.destroyAllWindows()

photo=cv2.imread('wm.jpg')
photo1=cv2.imread('bts-pic1.jpg')


#find the shape of images 
print(photo.shape)
print(photo1.shape)

#resize watermark to bigger image size
photo=cv2.resize(photo,(341,605))

cv2.imshow('title',photo)
cv2.imshow('title1',photo1)
cv2.waitKey()    
cv2.destroyAllWindows()

#to blend both images together
blend_photo = cv2.addWeighted(photo1, 0.8, photo, 0.2, 0)
cv2.imshow('blend',blend_photo)
cv2.imwrite('blend.jpg',blend_photo)
cv2.waitKey()    
cv2.destroyAllWindows()


#to add a picture bellow(vertically)
v_photo = cv2.vconcat([blend_photo, photo1])
cv2.imshow('vconcat.jpg', v_photo)
cv2.imwrite('vconcat.jpg', v_photo)
cv2.waitKey()    
cv2.destroyAllWindows()


#to add a picture side-by-side(horizontally)
h_photo = cv2.hconcat([blend_photo, photo1])
cv2.imshow('hconcat.jpg', h_photo)
cv2.imwrite('hconcat.jpg', h_photo)
cv2.waitKey()    
cv2.destroyAllWindows()
