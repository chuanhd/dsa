import pytest

from dsa.bubble_sort import bubble_sort

def test_bubble_sort():
  assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
  assert bubble_sort([3, 0, -2, 8, -1]) == [-2, -1, 0, 3, 8]
  assert bubble_sort([]) == []
  assert bubble_sort([1]) == [1]
  assert bubble_sort([2, 1]) == [1, 2]
  assert bubble_sort([4, 4, 4]) == [4, 4, 4]
  assert bubble_sort([10, 20, 30, 40]) == [10, 20, 30, 40]
  assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]