"""
    Otsu's Binarization

    In the simple thresholding, we select a global threshold that is arbitrarily selected. It is
    difficult to know what the right value of the threshold is, so we may need to do trial-and-
    error experiments a few times before you get the right value. Even if you get an ideal value
    for one case, it may not work with other images that have different pixel intensity characteristics.
    Otsu’s method determines an optimal global threshold value from the image histogram. For now, just
    think of the histogram as the frequency distribution of pixel values.
"""

# Otsu's Binarization

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY, threshold,
                 THRESH_BINARY, THRESH_OTSU, THRESH_BINARY_INV)
