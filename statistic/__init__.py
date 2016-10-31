# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, division

import copy
import math


def mean(list_of_values):
    """return a mean of values inside data set"""
    return sum(list_of_values)/len(list_of_values)


def mode(list_of_values):
    """ return the value most common inside data set"""
    unique_values = set(list_of_values)
    indice_dict = {}
    for value in unique_values:
        indice_dict[value] = list_of_values.count(value)

    keys_in_dict = sorted(
        [(key, value) for key, value in indice_dict.iteritems()],
        key=lambda x: x[1])

    # return value in end of list, sorted by number of occurrences
    return keys_in_dict[-1][0]


def median(list_of_values):
    copy_list = copy.deepcopy(list_of_values)
    copy_list.sort()
    many_items = len(copy_list)
    half_list = int(many_items/2)
    if many_items % 2 == 0:
        centered_values = copy_list[half_list-1:half_list+1]
        copy_list.insert(half_list, sum(centered_values)/2)

    return copy_list[half_list]


def calculate_quartile(list_of_values, third_quartile=False):
    """Generic formula to get a quartile, first or third quartile """
    copy_list = copy.deepcopy(list_of_values)
    copy_list.sort()
    many_items = len(copy_list)
    half_list = int(many_items/2)
    print half_list
    if third_quartile:
        half_list_of_values = copy_list[half_list:]
    else:
        half_list_of_values = copy_list[:half_list]

    print half_list_of_values
    quartile = median(half_list_of_values)
    return quartile


def interquartile(list_of_values):
    copy_list = copy.deepcopy(list_of_values)
    copy_list.sort()
    many_items = len(copy_list)
    half_list = int(many_items/2)
    if many_items % 2 == 0:
        copy_list.insert(half_list, median(copy_list))

    first_quartile = calculate_quartile(copy_list)
    third_quartile = calculate_quartile(copy_list, third_quartile=True)
    return third_quartile - first_quartile


def standard_deviation(list_of_values):
    return math.sqrt(variance(list_of_values))


def variance(list_of_values):
    mean_ = mean(list_of_values)
    sum_of_squares = sum([(item - mean_)**2 for item in list_of_values])
    return sum_of_squares/(len(list_of_values) - 1)


def z_score(list_of_values, value_to_score):
    mean_value = mean(list_of_values)
    S_deviation = standard_deviation(list_of_values)
    return (value_to_score - mean_value)/S_deviation


def pearson_r(x_values, y_values):
    total_sum = 0
    for i, item in enumerate(x_values):
        total_sum += z_score(x_values, item) * z_score(y_values, y_values[i])
    return total_sum/(len(x_values) - 1)


def slope(x_values, y_values):
    pearson = pearson_r(x_values, y_values)
    # Standard deviation for X values
    Sx = standard_deviation(x_values)

    Sy = standard_deviation(y_values)
    return pearson * (Sy/Sx)


def constant(x_values, y_values):
    b = slope(x_values, y_values)
    return mean(y_values) - b * mean(x_values)


def linear_regression(x_values, y_values, value_x_predict):
    a = constant(x_values, y_values)
    b = slope(x_values, y_values)
    predicted_y = a + b * value_x_predict
    return predicted_y


def r_squared(x_values, y_values):
    return pearson(x_values, y_values) ** 2
