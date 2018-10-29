# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import itertools


def integrate_perimeters(data):

    """ Integrate perimeters of all triangles in the sample. """

    data = list(itertools.chain.from_iterable(data))
    return data


def drop_zero(data):

    """ Drop non-numbers in the data """

    data_new = []
    for i in range(len(data)):
        if data[i] != 0:
            data_new.append(data[i])
    return data_new


def preprocess(data):

    """
    step1. Replace the non values to zeros.
    step2. Reshape perimeters from a matrix to a vector.
    step3. Drop all zeros.
    """

    data = data.fillna(0)
    data = np.array(data.loc[:].values)
    data = integrate_perimeters(data)
    data = drop_zero(data)

    return data


def plot_hist(data, file, bins=5):

    """ Plot the histogram """

    plt.figure()
    plt.hist(data, bins=bins)
    plt.xlabel('Perimeter')
    plt.ylabel('Frequency')
    hist_name = 'figure/' + file[5:-5] + '.png'
    plt.savefig(hist_name)


# Read perimeters from excel file.
filename = 'data/sample02.xlsx'
perimeters = pd.read_excel(filename, index_col=0)

# Preprocess perimeters.
perimeters = preprocess(perimeters)

# Plot histogram.
plot_hist(perimeters, filename, bins=10)
