import cv2
import numpy as np 

def clipped_addition(img, x, _max=255, _min=0):
  if x > 0:
    mask = img > (_max - x)
    img += x
    # inserts _max into img where mask predicate is true
    np.putmask(img, mask, _max)

  if x < 0:
    mask = img < (_min - x)
    img += x
    # inserts _min into img where mask predicate is true
    np.putmask(img, mask, _max)

def regulate(img, hue=0, saturation=0, luminosity=0):
  # HSV_FULL has hues 0-360, while HSV has hues 0-180
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)

  if hue < 0:
    hue = 255 + hue

  # gives the whole array with 3rd dimension of 0 height (3 dimensional array)
  hsv[:, :, 0] += hue
  # we don't change hue if hue > 0

  # regulate saturation and luminosity
  clipped_addition(hsv[:, :, 1], saturation)
  clipped_addition(hsv[:, :, 2], luminosity)

  # hue vs saturation vs luminosity?

  return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR_FULL)