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


def calculate_quartile(list_of_values, end=False):
    """Generic formula to get a quartile, first or third quartile """
    copy_list = copy.deepcopy(list_of_values)
    copy_list.sort()
    many_items = len(copy_list)
    half_list = int(many_items/2)
    print half_list
    if end:
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
    third_quartile = calculate_quartile(copy_list, end=True)
    return third_quartile - first_quartile


def standard_deviation(list_of_values):
    return math.sqrt(variance(list_of_values))

def variance(list_of_values):
    mean_ = mean(list_of_values)
    sum_of_squares = sum([(item - mean_)**2 for item in list_of_values])
    return sum_of_squares/(len(list_of_values) - 1)
