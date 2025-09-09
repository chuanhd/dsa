from typing import List

class Solution:
    # Brute-force solution
    # def largestRectangeArea(self, height: List[int]) -> int:
    #     max_rect = 0
    #     len_h = len(height)
    #     for i in range(len_h):
    #         left, right = i, i
    #         for j in range(i, 0, -1):
    #             if height[j] >= height[i]:
    #                 left = j
    #             else:
    #                 break
    #         for j in range(i + 1, len_h):
    #             if height[j] >= height[i]:
    #                 right = j
    #             else:
    #                 break
    #         s = height[i] * (right - left + 1)
    #         max_rect = max(max_rect, s)
    #
    #     return max_rect
    #

    def largestRectangeArea(self, heights: List[int]) -> int:
        s = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while s and s[-1][1] > h:
                index, height = s.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            s.append((start, h))

        for i, h in s:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area;


if __name__ == "__main__":
    solution = Solution()

    print(solution.largestRectangeArea([7, 1, 7, 2, 2, 4]))
