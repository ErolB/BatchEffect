cimport numpy as np
from numpy import percentile, zeros
import copy

def batch_correction(reference, other_frame):
    marker_coefs = {}
    for marker in reference.columns:
        coefs = []
        for i in range(100):
            a = percentile(reference[marker], i)
            b = percentile(other_frame[marker], i)
            if (a!=0) and (b!=0):
                coefs.append(a/b)
            else:
                coefs.append(0)
        marker_coefs[marker] = coefs
    return marker_coefs

def apply_transformation(original_data, marker_coefs):
    data = copy.copy(original_data)
    size = len(marker_coefs['CD16'])
    cdef float lower_bound
    cdef float upper_bound
    cdef float current_value
    cdef int i, j
    cdef float k
    cdef np.ndarray new_marker_data, marker_data
    for marker in data.columns:
        coefs = marker_coefs[marker]
        marker_data = data[marker].values
        new_marker_data = zeros(len(marker_data))
        for i in range(100):
            print(i)
            lower_bound = percentile(marker_data, i)
            upper_bound = percentile(marker_data, i+1)
            k = coefs[i]
            for j in range(len(marker_data)):
                current_value = marker_data[j]
                if (current_value > lower_bound) and (current_value < upper_bound):
                    new_marker_data[j] = current_value * k
            print('finished')
        data[marker] = new_marker_data
    return data
