"""
    Gradients and Edge Detection

    Edge detection methods:
        - Finding gradients
        - Canny edge detection

    Finding gradients:
        - Sobel derivatives
        - Laplacian derivatives

    Sobel derivatives:
        The Sobel method is a combination of Gaussian smoothing and Sobel differentiation, which computes
        an approximation of the gradient of an image intensity function. Because of the Gaussian smoothing,
        this method is resistant to noise. We can perform derivatives either in the horizontal or vertical
        direction by passing the arguments xorder and yorder, respectively. The Sobel() function also takes
        an argument ksize that we use to define the kernel size. If we set ksize to -1, OpenCV will internally
        apply a 3×3 Schar filter, which generally gives a better result compared to the 3×3 Sobel filter.
"""

# Sobel derivatives

from cv2 import (imread, imshow, waitKey, cvtColor, COLOR_BGR2GRAY, bilateralFilter,
           Sobel, CV_64F)
from numpy import (uint8, absolute)


# Loading the image and converting to grayscale
original_image = imread("images/sudoku.png")
grayscale_image = cvtColor(original_image, COLOR_BGR2GRAY)
# Applying bilateral filter
blurred_image = bilateralFilter(grayscale_image, 5, 50, 50)
imshow("Blurred Image", blurred_image)


# Sobel gradient detection
sobel_x = Sobel(blurred_image, CV_64F, 1, 0, ksize=3)
sobel_x = uint8(absolute(sobel_x))
sobel_y = Sobel(blurred_image, CV_64F, 0, 1, ksize=3)
sobel_y = uint8(absolute(sobel_y))
imshow("Sobel X", sobel_x)
imshow("Sobel Y", sobel_y)

# Schar gradient detection by passing ksize = -1 to Sobel function
schar_x = Sobel(blurred_image, CV_64F, 1, 0, ksize=-1)
schar_x = uint8(absolute(schar_x))
schar_y = Sobel(blurred_image, CV_64F, 0, 1, ksize=-1)
schar_y = uint8(absolute(schar_y))
imshow("Schar X", schar_x)
imshow("Schar Y", schar_y)
waitKey(0)
