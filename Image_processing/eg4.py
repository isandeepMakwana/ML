import cv2

imageData = cv2.imread("images/image_1.jpeg")
for r in range(imageData.shape[0]):
    for c in range(imageData.shape[1]):
        rgb = imageData[r][c]
        red = int(rgb[0])
        green = int(rgb[1])
        blue = int(rgb[2])
        if red < green:
            clr = red
        else:
            clr = green
        if clr > blue:
            clr = blue
        imageData[r][c] = (clr, clr, clr)  # image file data is being manipulated
cv2.imwrite("tmpfile.jpg", imageData)
print("done")
