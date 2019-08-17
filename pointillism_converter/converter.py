import cv2
from pointillism_converter import *

img = cv2.imread("images/house.jpg")

colors = ColorPalette.extract_colors(img, 2)
# remember to explore different clustering techniques and learn VQ

colors = colors.extend([(0, 50, 0), (15, 30, 0), (-15, 30, 0)])