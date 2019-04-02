import cv2
import numpy as np
img = cv2.imread('w1p.png',1)
output = img.copy()
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(cimg,100,150)

# for (i, j) in rads:
circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,
                            param1=60,param2=24,minRadius=1, maxRadius=50)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(output,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)



circles1 = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=32,minRadius=50, maxRadius=90)

if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in circles1[0,:]:
        # draw the outer circle
        cv2.circle(output,(i[0],i[1]),i[2],(0,255,255),2)
        # draw the center of the circle
        cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)


circles1 = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,
                            param1=60,param2=43,minRadius=90, maxRadius=160)
if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in circles1[0,:]:
        # draw the outer circle
        cv2.circle(output,(i[0],i[1]),i[2],(0,0,255),2)
        # draw the center of the circle
        cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)

circles1 = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,
                            param1=40,param2=33,minRadius=140, maxRadius=210)
if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in circles1[0,:]:
        # draw the outer circle
        cv2.circle(output,(i[0],i[1]),i[2],(255,0,0),2)
        # draw the center of the circle
        cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected circles',output)
cv2.waitKey(0)
cv2.destroyAllWindows()