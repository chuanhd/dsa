import pytest

from dsa.insertion_sort import insertion_sort

def test_insertion_sort():
    assert insertion_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert insertion_sort([3, 0, -2, 8, -1]) == [-2, -1, 0, 3, 8]
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([2, 1]) == [1, 2]
    assert insertion_sort([4, 4, 4]) == [4, 4, 4]
    assert insertion_sort([10, 20, 30, 40]) == [10, 20, 30, 40]
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]