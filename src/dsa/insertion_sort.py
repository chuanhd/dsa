def insertion_sort(nums: list[int]) -> list[int]:
  """
  Insertion Sort Algorithm Implementation
  Time Complexity: O(n^2)
  Space Complexity: O(1)
  Stable: Yes
  """

  n = len(nums)
  for i in range(1, n):
    base = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > base:
      nums[j + 1] = nums[j]
      j -= 1
    nums[j + 1] = base

  return nums;