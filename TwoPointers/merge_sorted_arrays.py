def merge_two_sorted(nums1, nums2):
  bot = 0
  top = 0
  result = []
  while top < len(nums1) and bot < len(nums2):
    # print(nums1[top], top, nums2[bot], bot)
    if nums1[top] < nums2[bot]:
      result.append(nums1[top])
      top += 1
    elif nums2[bot] >= nums1[top]:
      result.append(nums2[bot])
      bot += 1
  
  while bot < len(nums2):
    result.append(nums2[bot])
    bot += 1
  while top < len(nums1):
    result.append(nums1[top])
    top += 1
  return result

# result = merge_two_sorted([1,2,3], [2,5,6])
# print(result)

# result = merge_two_sorted([1,1,1], [2,5,6])
# print(result)

# result = merge_two_sorted([1,1,1], [1,1,1])
# print(result)


def merge(nums1, m, nums2, n):
  i = len(nums1) - 1
  while n > 0 and m > 0:
    if nums2[n - 1] > nums1[m - 1]:
      nums1[i] = nums2[n - 1]
      n -= 1
    else:
      nums1[i] = nums1[m - 1]
      m -= 1
    i -= 1
  # print(n, m, i)
  while n > 0:
    nums1[i] = nums2[n - 1]
    n, i = n - 1, i - 1
  # print(nums1)
merge([1,2,3,0,0,0], 3, [2,5,6], 3)
merge([2,2,3,0,0,0], 3, [1,5,6], 3)
