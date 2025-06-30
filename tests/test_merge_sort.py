import pytest 

from dsa.merge_sort import merge_sort

def test_merge_sort():
    assert merge_sort([3, 6, 8, 10, 1, 2, 1], 0, 6) == [1, 1, 2, 3, 6, 8, 10]
    assert merge_sort([5], 0, 0) == [5]
    assert merge_sort([], 0, 0) == []
    assert merge_sort([2, 1], 0, 1) == [1, 2]
    assert merge_sort([4, 3, 2, 1], 0, 3) == [1, 2, 3, 4]
    assert merge_sort([1.5, 2.5, -0.5], 0, 2) == [-0.5, 1.5, 2.5]
    assert merge_sort([1, 2, 3, 4, 5], 0, 4) == [1, 2, 3, 4, 5]