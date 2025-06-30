def quick_sort(nums: list[int], left: int, right: int) -> list[int]:
  if left >= right:
    return nums
  
  if len(nums) <= 1:
    return nums

  pivot = partition(nums, left, right)
  print(f"pivot: {pivot}, nums: {nums}")
  # Recursively sort the two sub-arrays
  quick_sort(nums, left, pivot - 1)
  quick_sort(nums, pivot + 1, right)
  print(f"After sorting: {nums}")
  return nums

def partition(nums: list[int], left: int, right: int) -> int:
  # Use left-most element as a pivot
  i, j = left, right
  print(f"Partitioning: {nums[left:right+1]}, left: {left}, right: {right}")
  print(f"Using pivot: {nums[left]} at index {left}")
  while i < j:
    while i < j and nums[j] >= nums[left]: # Keep pointer moving to the left to find out the first element smaller than the pivot
      j -= 1
    while i < j and nums[i] <= nums[left]: # Keep pointer moving to the right to find out the first element larger than the pivot
      i += 1
    # Swap element
    print(f"Swapping {nums[i]} at {i} and {nums[j]} at {j}")
    nums[i], nums[j] = nums[j], nums[i]
    print(f"nums: {nums}")
  # Swap the pivot to the boundary between the two sub-arrays
  nums[i], nums[left] = nums[left], nums[i]

  return i # return index of the pivot