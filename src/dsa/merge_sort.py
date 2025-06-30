def merge_sort(nums: list[int], left: int, right: int):
  if left >= right:
    return nums
  
  mid = left + (right - left) // 2 # "//" is floor division operator 
  merge_sort(nums, left, mid)
  merge_sort(nums, mid + 1, right)
  merge(nums, left, mid, right)

  return nums

def merge(nums: list[int], left: int, mid: int, right: int):
  print(f"Merging: {nums[left:right+1]}, left: {left}, mid: {mid}, right: {right}")
  tmp = [0] * (right - left + 1)
  left_nums = nums[left:mid+1]
  right_nums = nums[mid+1:right+1]
  print(f"Left sub-array: {left_nums}, Right sub-array: {right_nums}")
  # i is the pointer of left_nums
  # j is the pointer of right_nums
  # k is the pointer of tmp
  i, j, k = 0, 0, 0
  while i < len(left_nums) and j < len(right_nums):
    if left_nums[i] <= right_nums[j]:
      tmp[k] = left_nums[i]
      i += 1
    else:
      tmp[k] = right_nums[j]
      j += 1
    k += 1
  print(f"Temporary merged array: {tmp[:k]}")
  # Copy the remaining elements of the left and right sub-arrays into the temporary array
  while i < len(left_nums):
    tmp[k] = left_nums[i]
    k += 1
    i += 1
  print(f"Temporary merged array after left sub-array: {tmp[:k]}")
  while j < len(right_nums):
    tmp[k] = right_nums[j]
    k += 1
    j += 1
  print(f"Temporary merged array after right sub-array: {tmp[:k]}")
  # Copy the temporary array back to the original array
  for i in range(len(tmp)):
    nums[left + i] = tmp[i]

def main():
  nums = [3, 6, 8, 10, 1, 2, 1]
  print(f"Original array: {nums}")
  print(f"Sorted array: {merge_sort(nums, 0, len(nums) - 1)}")

if __name__ == "__main__":
  main()
  # The main function is for testing purposes, it can be removed in production code.


  