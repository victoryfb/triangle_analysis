# -*- coding:utf-8 -*-
import cv2
import numpy as np


def preprocess_img(filename):

    """
    Get binary image
    """
    # Load image
    img = cv2.imread(filename)

    # Change the color space from RGB to GRAY
    GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Median blur
    GrayImage = cv2.medianBlur(GrayImage, 5)

    # Contrast enhancement (Laplace)
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    GrayImage = cv2.filter2D(GrayImage, cv2.CV_8UC3, kernel)

    # Get the binary image out of a grayscale image.
    # ret, th1 = cv2.threshold(GrayImage, 115, 200, cv2.THRESH_BINARY_INV)
    ret, th1 = cv2.threshold(GrayImage, 115, 200, cv2.THRESH_BINARY)
    filename_pro = 'img/preprocessed/' + filename[13:-4] + '_pro.png'

    cv2.imwrite(filename_pro, th1)

    return filename_pro
