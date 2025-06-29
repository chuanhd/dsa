import pytest

from dsa.selection_sort import selection_sort

def test_selection_sort():
    assert selection_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert selection_sort([3, 0, -2, 8, -1]) == [-2, -1, 0, 3, 8]
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([2, 1]) == [1, 2]
    assert selection_sort([4, 4, 4]) == [4, 4, 4]
    assert selection_sort([10, 20, 30, 40]) == [10, 20, 30, 40]
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]