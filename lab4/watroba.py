import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('w1ppp.png',1)
height, width, channels = img.shape
output = cv2.imread('w1.png',1)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(cimg,100,150)


area = 0.0

arr = []

# for (i, j) in rads:
circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,
                            param1=60,param2=9,minRadius=3, maxRadius=30)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(output,(i[0],i[1]),i[2],(0,255,0),2)
        area += np.pi * i[2]*i[2]
        arr.append(i[2])
        
        # draw the center of the circle
        cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',output)
print(area / (height*width))
plt.hist(arr)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()