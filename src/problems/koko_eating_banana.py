# 875. Koko eating banana

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            spend = 0
            for p in piles:
                spend += math.ceil(p / k)

            if spend <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res

if __name__ == "__main__":
    solution = Solution()

    print(solution.minEatingSpeed([3, 6, 7, 11], 8))
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))
    print(solution.minEatingSpeed([2, 2], 2))
    print(solution.minEatingSpeed([1, 4, 3, 2], 9))
