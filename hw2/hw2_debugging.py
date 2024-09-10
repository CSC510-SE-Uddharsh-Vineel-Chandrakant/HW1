"""
This Module is for implementing the merge sort algorithm.
"""

import rand

def merge_sort(arr):
    """
    This function performs the merge sort.
    Args:
        arr(list): The array to sort.
    Returns:
        list: A sorted version of the input array.
    """
    if len(arr) == 1:
        return arr

    half = len(arr) // 2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    """
    This function Combines two sorted arrays into a single sorted array.

    Args:
        left_arr(list): The left half of the array.
        right_arr(list): The right half of the array.

    Returns:
        list: A merged sorted array.
    """
    left_index = 0
    right_index = 0
    merged_array = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_array[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merged_array[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merged_array[left_index + right_index] = right_arr[i]
        right_index += 1

    for i in range(left_index, len(left_arr)):
        merged_array[left_index + right_index] = left_arr[i]
        left_index += 1

    return merged_array


array = rand.random_array([None] * 20)
arr_out = merge_sort(array)

print(arr_out)
