# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def triangle_filter(side1, side2, side3):

    """ Judge the approximate equilateral triangle """

    error1 = np.abs(side1 - side2)
    error2 = np.abs(side1 - side3)
    error3 = np.abs(side2 - side3)
    if (error1 + error2 + error3) > (0.1 * (side1 + side2 + side3)):
        return False
    else:
        return True


def calculate_triangle_perimeter(corner1, corner2, corner3):

    """ Calculate the perimeter of triangle """

    side1_length = np.sqrt((corner1[0][0] - corner2[0][0]) ** 2 + (corner1[0][1] - corner2[0][1]) ** 2)
    side2_length = np.sqrt((corner1[0][0] - corner3[0][0]) ** 2 + (corner1[0][1] - corner3[0][1]) ** 2)
    side3_length = np.sqrt((corner2[0][0] - corner3[0][0]) ** 2 + (corner2[0][1] - corner3[0][1]) ** 2)
    triangle_perimeter = side1_length + side2_length + side3_length
    return side1_length, side2_length, side3_length, triangle_perimeter


def draw_text_info(shapes, image):

    """ Draw the index of triangle and the number of triangle on the picture """

    c1 = shapes['triangle']
    cv.putText(image, "triangle: " + str(c1), (50, 70), cv.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 2)
    return image


def analysis(shapes, original_img, precessed_img):

    """ Analyze triangles in the picture """

    # Load the image.
    result = cv.imread(original_img)
    frame = cv.imread(precessed_img)

    # Perimeter of each triangle.
    perimeters = []

    # h, w, ch = frame.shape
    # result = np.zeros((h, w, ch), dtype=np.uint8)
    # result = cv.imread()

    # Get the binary image
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

    # edge = cv.Canny(binary, 50, 150)

    # Find all contours in the image.
    # out_binary, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    print("Start to detect triangle shape...\n")

    for cnt in range(len(contours)):

        # Find triangle using approximation method.
        epsilon = 0.023 * cv.arcLength(contours[cnt], True)
        approx = cv.approxPolyDP(contours[cnt], epsilon, True)

        # Analyze the shape.
        corners = len(approx)

        if corners == 3:
            # Save the number of triangles.
            count = shapes['triangle']

            corner1 = approx[0]
            corner2 = approx[1]
            corner3 = approx[2]

            # Calculate the perimeter.
            # p = cv.arcLength(contours[cnt], True)
            s1, s2, s3, p = calculate_triangle_perimeter(corner1, corner2, corner3)

            flag = triangle_filter(s1, s2, s3)

            if p > 50 and flag:
                count = count + 1
                shapes['triangle'] = count
                perimeters.append(p)

                # Draw the contour.
                # cv.drawContours(result, contours, cnt, (0, 0, 255), 2)
                corner1 = (corner1[0][0], corner1[0][1])
                corner2 = (corner2[0][0], corner2[0][1])
                corner3 = (corner3[0][0], corner3[0][1])
                cv.line(result, corner1, corner2, (0, 0, 255), thickness=2)
                cv.line(result, corner1, corner3, (0, 0, 255), thickness=2)
                cv.line(result, corner2, corner3, (0, 0, 255), thickness=2)

                # Give the label of each triangle.
                mm = cv.moments(contours[cnt])
                cx = int(mm['m10'] / mm['m00'])
                cy = int(mm['m01'] / mm['m00'])
                cv.putText(result, str(len(perimeters)), (cx, cy), cv.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 2)

    # Save the result image.
    filename_result = 'img/result/' + precessed_img[17:-8] + '_result.png'
    cv.imwrite(filename_result, draw_text_info(shapes, result))

    return perimeters

