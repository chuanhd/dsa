import pytest

from dsa.quick_sort import quick_sort

def test_quick_sort():
    assert quick_sort([3, 6, 8, 10, 1, 2, 1], 0, 6) == [1, 1, 2, 3, 6, 8, 10]
    assert quick_sort([5], 0, 0) == [5]
    assert quick_sort([], 0, -1) == []
    assert quick_sort([2, 1], 0, 1) == [1, 2]