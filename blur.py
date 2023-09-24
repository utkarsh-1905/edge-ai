import imutils
import cv2
import numpy as np

i=cv2.imread('/home/csed/Desktop/Edge_AI/Accelerated AI/Lab/sudoku.jpeg')
blurImg = cv2.blur(i,(3,3)) 
cv2.imshow('Original image',i)
  
cv2.waitKey(0)
cv2.imshow('blurred image',blurImg)
  
cv2.waitKey(0)

