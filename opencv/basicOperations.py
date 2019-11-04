import cv2 as cv
import numpy as np

fileName0 = "C:\\Users\\nvt-pc\\Desktop\\1.png"
fileName1 = "C:\\Users\\nvt-pc\\Desktop\\1_0.png"

img = cv.imread(fileName0)

# 图像：高、宽、channelimport cv2 as cv
import numpy as np

fileName0 = "C:\\Users\\nvt-pc\\Desktop\\1.png"
fileName1 = "C:\\Users\\nvt-pc\\Desktop\\1_0.png"

img = cv.imread(fileName0)

# 图像：高、宽、channel
print(img.shape)
# w*h*channel && dtype
print(img.size, img.dtype)
# 像素取值
pixel = img[100, 100]
# pixel_blue = img[100,100,0]
# 图像通道分割
b, g, r = cv.split(img)
# b = img[:,:,0]
# 图像高、宽
h, w = img.shape[0:2]
# 图像缩放
img_resize = cv.resize(img, (50, 50), cv.INTER_AREA)
# 颜色空间变换
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 保存图像
cv.imwrite(fileName1, gray)
# 图像ROI
region = img[20:30, 60:90]




print(img.shape)
# 像素取值
pixel = img[100, 100]
# 图像通道分割
b, g, r = cv.split(img)
# 图像高、宽
h, w = img.shape[0:2]
# 图像缩放
img_resize = cv.resize(img, (50, 50), cv.INTER_AREA)
# 颜色空间变换
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 保存图像
cv.imwrite(fileName1, gray)



