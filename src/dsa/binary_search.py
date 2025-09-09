from typing import List
import math

def binary_search(nums: List[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    result = -1

    while i < j:
        m = math.floor((i + j) / 2)
        if target < nums[m]:
            j = m - 1
        elif target > nums[m]:
            i = m + 1
        else:
            return m

    return result
