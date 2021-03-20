class Solution:
  def containsDuplicate(self, nums) -> bool:
    bucket = {}
    for val in nums:
      bucket[val] = 0
    for val in nums:
      bucket[val] += 1
    
    hasTwice = False
    for _, val in bucket.items():
      if (val > 1):
        hasTwice = True
        break
    return hasTwice