# /usr/bin/env python3
# -*- coding: utf-8 -*-

import statistics
import math

data = [2, 2, 3, 3, 3]
variance_value = statistics.variance(data)
print("方差:", variance_value)

def manual_variance(data):
    mean = statistics.mean(data)
    sum_value = sum([math.pow(x - mean, 2) for x in data])
    variance_value_manual = sum_value / (len(data) - 1)
    return variance_value_manual

variance_value = manual_variance(data)
print("手动方差:", variance_value)
