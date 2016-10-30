# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, division

import copy

def mean(list_of_values):
    return sum(list_of_values)/len(list_of_values)


def median(list_of_values):
    copy_list = copy.deepcopy(list_of_values)
    copy_list.sort()
    many_items = len(copy_list)
    half_list = int(many_items/2)
    if many_items % 2 == 0:
        centered_values = copy_list[half_list-1:half_list+1]
        copy_list.insert(half_list, sum(centered_values)/2)

    return copy_list[half_list]


def interquatile(list_of_values):
    copy_list = copy.deepcopy(list_of_values)
    copy_list.sort()
    many_items = len(copy_list)
    half_list = int(many_items/2)
    if many_items % 2 == 0:
        copy_list.insert(half_list, median(copy_list))

    first_quartile = median(copy_list[:half_list])
    third_quartile = median(copy_list[half_list+1:])
    return third_quartile - first_quartile
