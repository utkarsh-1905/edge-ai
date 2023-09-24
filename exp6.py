import imutils
import cv2
import numpy as np
from PIL import Image,ImageFilter


i=Image.open('/home/csed/Desktop/Edge_AI/Accelerated AI/Lab/sudoku.jpeg')
i.filter(ImageFilter.MinFilter(size=25))
i.save('fil2.png')
#implement max,median filters
