def bubble_sort(nums: list[int]) -> list[int]:
    """
    Bubble Sort Algorithm Implementation
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    Stable: Yes
    """
    n = len(nums)
    for i in range(n - 1, 0, -1):
      for j in range (i):
        if nums[j] > nums[j + 1]:
          nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)    
    return nums