import cv2
import numpy as np

img_path = "./images/tianjin.jpg"

img = cv2.imread(img_path)

(h, w, _) = img.shape

# how does (5, 5) affect the blur?
gBlur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)

cv2.imshow("image", gBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()
