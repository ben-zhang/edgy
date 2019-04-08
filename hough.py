import cv2
import numpy as np

img = cv2.imread("./images/house.jpg")

# now we use canny edge detection to get a binary image.
# simple thresholding will work as well.

edgeMap = cv2.Canny(img, 100, 200)

# cv2.imshow("uncanny", edgeMap)
# cv2.waitKey(0)

"""
hough hough hough
args: image, rho (the p looking thing), theta accuracies (parametric equation of line),
      threshold(minimum vote for a line)
"""

hough = cv2.HoughLines(edgeMap, 1, np.pi/180, 500)
for line in hough:
  for rho, theta in line:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(edgeMap,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("lines", edgeMap)
cv2.waitKey(0)


# cv2.imshow("hough hough hough", hough)
# cv2.waitKey(0)
