"""
    Noise reduction using smoothing and blurring

    Bilateral blurring:
        The previous three blurring techniques yield blurred images with the side effect that we
        lose the edges in the image. To blur an image while preserving the edges, we use bilateral
        blurring, which is an enhancement over Gaussian blurring. Bilateral blurring takes two
        Gaussian distributions to perform the computation. The first Gaussian function considers
        the spatial neighbors (pixels in x and y space that are close together). The second Gaussian
        function considers the pixel intensity of the neighboring pixels. This makes sure that only
        those pixels that are of similar intensity to the central pixel are considered for blurring,
        leaving the edges intact as the edges tend to have higher intensity compared to other pixels.
"""

from cv2 import imread, imshow, waitKey, bilateralFilter

# Bilateral blurring
# Loading the noisy image
noisy_image = imread("images/salt_and_pepper_noise.jpg")
imshow("Noisy Image", noisy_image)

# Performing bilateral filter
# Bilateral blurring with diameter 5
filtered_image_5 = bilateralFilter(noisy_image, 5, 150, 50)
imshow("Blurred Image with diameter 5", filtered_image_5)

# Bilateral blurring with diameter 7
filtered_image_7 = bilateralFilter(noisy_image, 7, 160, 60)
imshow("Blurred Image with diameter 7", filtered_image_7)
waitKey(0)
