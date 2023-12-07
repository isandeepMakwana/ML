# convert to grayscale
import cv2
imageData = cv2.imread("images/image_2.jpeg")
for r in range(imageData.shape[0]):
    for c in range(imageData.shape[1]):
        rgb = imageData[r][c]
        red= int(rgb[0])
        green = int(rgb[1])
        blue = int(rgb[2])
# method 1
        avg = (red+green+blue)/3
        imageData[r][c] = (avg,avg,avg)
cv2.imwrite("tmpfile.jpg",imageData)
