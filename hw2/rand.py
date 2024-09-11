"""
This module is for generating a random array of numbers.
"""

import subprocess

def random_array(arr):
    """
    Produces a random array by shuffling the numbers between 1 and 20.

    Args:
        arr (list): A list with 0 elements to be filled with random numbers.

    Returns:
        list: A list filled with random numbers.
    """
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
