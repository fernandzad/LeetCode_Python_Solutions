# 217. Contains Duplicate
# Set
# https://leetcode.com/problems/contains-duplicate/
# O(n)
def containsDuplicate(nums):
  hash = set()
  for item in nums:
    if item in hash:
      return True
    hash.add(item)
  return False