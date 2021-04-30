"""
    Noise reduction using smoothing and blurring

    Smoothing, also called blurring, is an important image processing technique to reduce
    noise present in an image.

    Types of noise that we encounter in an image:
        - Salt and pepper noise
        - Impulse noise
        - Gaussian noise
"""

from cv2 import blur, imread, imshow, waitKey

# Loading the image
original_image = imread("images/918_spyder.jpg")
imshow("Original Image", original_image)
