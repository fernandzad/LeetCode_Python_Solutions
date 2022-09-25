# 1. Two Sum
# HashMap 
# https://leetcode.com/problems/two-sum/
# O(n)

def twoSum(nums, target):
  hash = dict()
  ans = []
  for i in range(len(nums)):
    hash[nums[i]] = i
  for i in range(len(nums)):
    key = target - nums[i]
    index = hash.get(key, -1)
    if index != -1 and index != i:
      ans.append(i)
      ans.append(index)
      break
  return ans