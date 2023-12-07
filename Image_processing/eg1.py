import cv2
imageData = cv2.imread("images/image_2.jpeg")
print(imageData)
print(type(imageData))
print(imageData.shape)
print(imageData[0][0])