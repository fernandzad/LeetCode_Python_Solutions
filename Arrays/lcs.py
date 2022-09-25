def longestConsecutive(nums):
  if len(nums) == 0:
    return 0
  uniqueNumbers = set(nums)
  maxLongestConsecutiveSequence = -1<<30

  for n in nums:
    longest = 1
    next = n + 1
    # THIS is the most important optimization
    # Avoid to run the algorithm for those numbers that are between our sequence
    # we want to run the algorithm only in the starting point, i.e. in this case for the 1
    if (n - 1) not in uniqueNumbers:
      while next in uniqueNumbers:
        longest += 1
        next += 1
      maxLongestConsecutiveSequence = max(maxLongestConsecutiveSequence, longest)
  return maxLongestConsecutiveSequence

longestConsecutive([100, 4, 200, 1, 3, 2])
longestConsecutive([0,3,7,2,5,8,4,6,0,1])