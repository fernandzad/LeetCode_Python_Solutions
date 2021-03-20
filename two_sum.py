# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# SOLUTION ver 2: O(n) time s 
def twoSum(nums, target):
  dictNums = {}
  for i, x in enumerate(nums):
    y = target - x
    if x in dictNums:
      return [dictNums[x], i]
    if y not in dictNums:
      dictNums[y] = i

# Tests cases    
print(twoSum([-1,-2,-3,-4,-5], -8))
print(twoSum([3, 3], 6))
print(twoSum([3, 2, 4], 6))
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 1, 4, 3], 6))

# SOLUTION ver 1 O(n^2) finding y
# def twoSum(nums, target):
#   l = len(nums)
#   ans = []
#   # dictNums = { i : nums[i] for i in range(0, len(nums) ) }
#   for i in range(l):
#     for j in range(i + 1, l):
#       if nums[i] + nums[j] == target:
#         ans.append(i)
#         ans.append(j)
#         return ans

# print(twoSum([3, 3], 6))
# print(twoSum([3, 2, 4], 6))
# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3, 1, 4, 3], 6))


    