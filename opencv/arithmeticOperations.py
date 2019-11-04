import cv2 as cv
import numpy as np

fileName0 = "C:\\Users\\nvt-pc\\Desktop\\1.png"
fileName1 = "C:\\Users\\nvt-pc\\Desktop\\1_0.png"

img = cv.imread(fileName0)

x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x, y))
print(x+y)
# dst = cv.addWeighted(img1,0.7,img2,0.3,0)

e1 = cv.getTickCount()
# your code execution
e2 = cv.getTickCount()
time = (e2 - e1)/cv.getTickFrequency()
print(time)



