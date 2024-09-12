from hw2_debugging import merge_sort
def test_merge_sort(regression):
    result = merge_sort([5, 2, 9, 1, 5, 6])
    regression.check(result)