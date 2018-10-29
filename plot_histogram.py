# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import itertools


def plot_hist(data, filename, bins=5):

    """ Plot the histogram """

    plt.figure()
    plt.hist(data, bins=bins)
    plt.xlabel('Perimeter')
    plt.ylabel('Frequency')
    hist_name = 'figure/' + filename[5:-5] + '.png'
    plt.savefig(hist_name)


def integrate_perimeters(perimeters):

    """ Integrate perimeters of all triangles in the sample. """

    perimeters = list(itertools.chain.from_iterable(perimeters))
    return perimeters


def drop_zero(data):

    """ Drop non-numbers in the data """

    data_new = []
    for i in range(len(data)):
        if data[i] != 0:
            data_new.append(data[i])
    return data_new


# Read perimeters from excel file.
filename = 'data/sample02.xlsx'
perimeters = pd.read_excel(filename, index_col=0)

# Replace the non values to zeros.
perimeters = perimeters.fillna(0)

# Reshape perimeters from a matrix to a vector.
perimeters = np.array(perimeters.loc[:].values)
perimeters = integrate_perimeters(perimeters)

# Drop all zeros.
perimeters = drop_zero(perimeters)

# Plot histogram
plot_hist(perimeters, filename, bins=10)
