
# Weighted method or luminosity method
import cv2
imageData = cv2.imread("images/image_2.jpeg")
for r in range(imageData.shape[0]):
    for c in range(imageData.shape[1]):
        rgb = imageData[r][c]
        red = (int(rgb[0])*0.3)
        green = (int(rgb[1])*0.59)
        blue = (int(rgb[2])*0.11)
        # imageData[r][c] = (red, green, blue)
        total = red + green + blue
        imageData[r][c] = (total, total, total)
cv2.imwrite("tmpfile.jpg", imageData)


