from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1
        while i <= j:
            m = (i + j) // 2
            sub_matrix = matrix[m]
            len_m = len(sub_matrix)
            min_e, max_e = sub_matrix[0], sub_matrix[len_m - 1]
            if target < min_e:
                j = m - 1
            elif target > max_e:
                i = m + 1
            else:
                return self.searchInnerMatrix(sub_matrix, target)

        return False

    def searchInnerMatrix(self, matrix: List[int], target: int) -> bool:
        i, j = 0, len(matrix) - 1
        while i <= j:
            m = (i + j) // 2
            if target < matrix[m]:
                j = m - 1
            elif target > matrix[m]:
                i = m + 1
            else:
                return True

        return False

if __name__ == "main":
    solution = Solution()
    print(solution.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))
