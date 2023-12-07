# import numpy
# a = numpy.zeros((10,3))
# print(a)

import numpy
import cv2

imageData = cv2.imread("images/image_1.jpeg")
cropFrom = (100, 200)
cropSize = (400, 300)

c1 = cropFrom[0]
r1 = cropFrom[1]
c2 = cropSize[0] - 1
r2 = cropSize[1] - 1

if r2 >= imageData.shape[0]:
    r2 = imageData.shape[0] - 1
if c2 >= imageData.shape[1]:
    c2 = imageData.shape[1] - 1

print("Actual Sie : ", imageData.shape)
cropSize = (c2 - c1 + 1, r2 - r1 + 1)
print(cropSize)
# print(imageData[0][0])
# newImage = numpy.zeros((cropSize[1], cropSize[0], 3))

r = r1
while r <= r2:
    print(r)
    imageData[r][c1] = (0, 0, 0)  # black bgr code
    imageData[r][c2] = (0, 0, 0)
    r += 1

c=c1
while c <=c2:
    print(c)
    imageData[r1][c] = (255,0,0)
    imageData[r2][c] = (255,0,0)
    c +=1

cv2.imwrite("tmp.jpeg", imageData)
print("Done")






# newImage = numpy.zeros((cropSize[1], cropSize[0], 3))
# # rr = 0
# # r = r1
# # while r <= r2:
# #     cc = 0
# #     c = c1
# #     while c <= c2:
# #         newImage[rr][cc] = imageData[r][c]
# #         cc += 1
# #         c += 1
# #     rr += 1
# #     r += 1

