#importing libraries
import cv2
import cv2 as cv


#Code to Read Image

img = cv.imread("UseImage.png")

#Edges
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray,5)
edges = cv.adaptiveThreshold(gray, 255,
                             cv.ADAPTIVE_THRESH_MEAN_C,
                             cv.THRESH_BINARY,9, 9)

#Cartooning
color = cv.bilateralFilter(img,9,250,250)
cartoon = cv2.bitwise_and(color,color, mask = edges)

cv.imshow("image", img)
cv.imshow("edges", edges)
cv.imshow("Cartoon", cartoon)
cv.waitKey(0)
cv.destroyAllWindows()
