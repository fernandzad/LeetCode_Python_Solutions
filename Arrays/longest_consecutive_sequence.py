# 128. Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums):
  if len(nums) == 0:
    return 0
  s = set(nums)
  max_sequence = -(1 << 30)
  for n in nums:
    long_sequence = 1

    # THIS is the most important optimization
    # Avoid to run the algorithm for those numbers that are between our sequence
    # we want to run the algorithm only in the starting point, i.e. in this case for the 
    if (n - 1) not in s:
      while (n + 1) in s:
        long_sequence += 1
        n += 1
      max_sequence = max(max_sequence, long_sequence)
  return max_sequence
  print(max_sequence)

longestConsecutive([100,4,200,1,3,2])
longestConsecutive([0,3,7,2,5,8,4,6,0,1])
