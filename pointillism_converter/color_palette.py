import cv2
import numpy as np
import math
from sklearn.cluster import KMeans
from .utils import regulate

class ColorPalette:
  def __init__(self, colors):
    self.colors = colors

# use k-means clustering to extract the n most common colors
  def extract_colors(img, n, max_size=200, n_init=10):
    # convert image to HSV color space
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    height, width, _ = img.shape

    # We don't really use this stuff, but it could go in reshape.
    resize_height = int(100 * height / max(width, height))
    resize_width = int(100 * width / max(width, height))

    img = cv2.resize(img, (resize_width, resize_height))

    # flatten image into an array of color values
    # We put -1 as input because it will infer the correct size
    img_arr = img.reshape((-1, 3))
    clt = KMeans(n_clusters = n, n_jobs = 1, n_init = n_init)
    clt.fit(img_arr)

    # Return a palette with these colors
    return ColorPalette(clt.cluster_centers_)

  def extend(self, extensions):
    # create extension to colors for each color by modifying hue, saturation, etc
    extension = [regulate(self.colors.reshape((1, len(self.colors), 3)).astype(np.uint8), *x).reshape((-1, 3)) for x in extensions]
    
    # append new colors onto color palette
    return ColorPalette(np.vstack([self.colors.reshape((-1, 3))] + extension))

    
    
