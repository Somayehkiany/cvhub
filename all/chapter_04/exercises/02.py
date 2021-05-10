"""
    Exercise 02:
        Create a histogram of a masked image
"""

from cv2 import (imread, imshow, waitKey, calcHist, rectangle)
import matplotlib.pyplot as plt
import numpy as np

# Loading the image
original_image = imread("../images/Bill-Gates.jpg")
imshow("Original Image", original_image)

# Creating the rectangular mask
mask_image = rectangle(np.zeros(original_image.shape[:2], dtype="uint8"), (50, 50),
                           (int(original_image.shape[1]) - 50, int(original_image.shape[0] / 2) - 50),
                           (255, 255, 255), -1)
imshow("Mask Image", mask_image)
