"""
    Adaptive Thresholding

    Adaptive thresholding is used to binarize a grayscale image that has a varying degree
    of pixel intensity, and one single threshold value may not be suitable to extract the
    information from the image. In adaptive thresholding, the algorithm determines the
    threshold for a pixel based on a small region around it. This will get us a different
    threshold value for different regions in the same image.
"""

# Adaptive Thresholding

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY, ADAPTIVE_THRESH_GAUSSIAN_C,
                 adaptiveThreshold, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, THRESH_BINARY_INV)


# Loading the image
original_image = imread("images/Abraham_Lincoln.jpg")
imshow("Original Image", original_image)

# Converting to grayscale
grayscale_image = cvtColor(original_image, COLOR_BGR2GRAY)
imshow("GrayScale Image", grayscale_image)

# Binarization using adaptive thresholding and simple mean
bsm = adaptiveThreshold(grayscale_image, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, 7, 3)
imshow("Binarization using adaptive thresholding and simple mean", bsm)

# Binarization using adaptive thresholding and Gaussian Mean
bgm = adaptiveThreshold(grayscale_image, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY_INV, 11, 3)
imshow("Binarization using adaptive thresholding and Gaussian Mean", bgm)
waitKey(0)
