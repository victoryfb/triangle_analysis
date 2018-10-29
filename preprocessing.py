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

    # Get the binary image out of a grayscale image.
    ret, th1 = cv2.threshold(GrayImage, 170, 255, cv2.THRESH_BINARY)

    filename_pro = 'img/preprocessed/' + filename[13:-4] + '_pro.png'

    cv2.imwrite(filename_pro, th1)

    """
    Reverse the color.
    """
    src = cv2.imread(filename_pro)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    img_info = src.shape
    image_height = img_info[0]
    image_weight = img_info[1]
    dst = np.zeros((image_height, image_weight, 1), np.uint8)
    for i in range(image_height):
        for j in range(image_weight):
            grayPixel = gray[i][j]
            dst[i][j] = 255-grayPixel

    cv2.imwrite(filename_pro, dst)

    return filename_pro
