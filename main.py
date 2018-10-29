# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from preprocessing import preprocess_img
from shape_analysis import analysis, plot_hist
from folders_operation import mkdir, file_name

# Create folders.
# mkdir('img/original')
# mkdir('img/preprocessed')
# mkdir('img/result')
# mkdir('figure')
# mkdir('data')

# Change the path of original_images every time.
original_images = file_name('img/original/sample02')
perimeters_all = []
for image in original_images:
    shapes = {'triangle': 0}
    image_preprocessed = preprocess_img(image)

    perimeters = analysis(shapes, image, image_preprocessed)
    print('************ ' + image + ' ************')
    print("The total number of triangles is ", len(perimeters))
    print('Perimeters are ')
    print(perimeters)
    perimeters_all.append(perimeters)

# Calculate the real length.
pass

# Save data to excel
result = pd.DataFrame(perimeters_all)
result.index = original_images
columns_name = np.arange(1, len(result.loc[original_images[0]]) + 1, 1)
result.columns = columns_name

file_path = original_images[0]
file_path = 'data/' + file_path[13:21] + '.xlsx'
writer = pd.ExcelWriter(file_path)
result.to_excel(writer, index=True, encoding='utf-8', sheet_name='Perimeters')


# Integrate perimeters of all triangles in the sample.
# perimeters_all = list(itertools.chain.from_iterable(perimeters_all))
#
# print('\n')
# print('************ ' + 'sample' + ' ************')
# print('Perimeters are ')
# print(perimeters_all)
# # Plot histogram of the sample.
# plot_hist(perimeters_all, original_images[0])

