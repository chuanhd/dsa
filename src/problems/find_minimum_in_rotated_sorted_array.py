# 153. Find minimum in rotated sorted bytearray

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

if __name__ == "__main__":
    solution = Solution()

    print(solution.findMin([3, 4, 5, 1, 2]))
    # print(solution.findMin([1, 2, 3, 4, 5]))
    # print(solution.findMin([3, 1, 2]))
    print(solution.findMin([5, 1, 2, 3, 4]))
    print(solution.findMin([2, 3, 1]))
