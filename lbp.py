import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./data/0009.png')
img_orig = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
b,g,r = cv2.split(img)

height, width, _ = img.shape

def getLocalPattern(img,center, i, j):
    try:
        if img[i][j] >= center:
            return 1
    except BaseException:
        pass
    return 0

def arrayToNumber(pattern):
    mul = 0
    number = 0
    pattern = np.flip(pattern)
    for i in pattern:
        number += i*(2**mul)
        mul += 1
    return number

def getLBP(img,i,j):
    center = img[i][j]

    pattern = []

    pattern.append(getLocalPattern(img,center, i-1,j+1))
    pattern.append(getLocalPattern(img,center, i,j+1))
    pattern.append(getLocalPattern(img,center, i+1,j+1))
    pattern.append(getLocalPattern(img,center, i+1,j))
    pattern.append(getLocalPattern(img,center, i+1,j-1))
    pattern.append(getLocalPattern(img,center, i,j-1))
    pattern.append(getLocalPattern(img,center, i-1,j-1))
    pattern.append(getLocalPattern(img,center, i-1,j))

    return arrayToNumber(pattern)

new_image = np.zeros((height,width),np.uint8)

for i in range(0,height):
    for j in range(0,width):
        new_image[i][j] = getLBP(b,i,j)
    
plt.subplot(121),plt.imshow(b),plt.title("Original")
plt.subplot(122),plt.imshow(new_image, cmap='gray'),plt.title("LBP")
plt.show()