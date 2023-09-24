import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./data/0020.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

alpha = 1
beta=5

# adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
# adjusted = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)

# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(adjusted),plt.title('Output')
# plt.show()

# Laplacian Sharpening

lsharp = cv2.Laplacian(img,cv2.CV_64F)
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(lsharp),plt.title('Output')
plt.show()