class Solution:
  def runningSum(self, nums):
    result = [sum(nums[:idx + 1]) for idx, val in enumerate(nums)]
    return result