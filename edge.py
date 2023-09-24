import cv2
import numpy as np


vid=cv2.VideoCapture(0)

while(True):

    ret,frame=vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_edge=cv2.Sobel(gray,cv2.CV_8U,1,1,ksize=5)
    cv2.imshow('frame_edge',np.uint8(255-frame_edge))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()