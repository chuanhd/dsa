# Selection Sort Algorithm Implementation
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Stable: No
def selection_sort(nums: list[int]):
  n = len(nums)
  for i in range(n - 1):
    k = i # Index of the minimum element
    # Find the index of the minimum element in the unsorted part of the array
    # Start from the next element after i
    # and go to the end of the array
    # This is the selection step
    for j in range(i + 1, n):
      if nums[j] < nums[k]: # Found a new minimum
        k = j # Update the index of the minimum element
    # Swap the found minimum element with the first element of the unsorted part
    nums[i], nums[k] = nums[k], nums[i]
  
  return nums