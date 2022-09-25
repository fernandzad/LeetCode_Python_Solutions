# 239. Sliding Window Maximum
from collections import deque

# TLE: Time Limit Exceeded
def maxSlidingWindow(nums, k):
  dq = deque() # indeces
  solution = []
  left = right = 0
  while right < len(nums):
    # pop smaller values in dq
    while dq and nums[dq[-1]] < nums[right]:
      dq.pop()
    dq.append(right)

    #remove left value from window
    if left > dq[0]:
       dq.popleft()

    if (right + 1) >= k:
      solution.append(nums[dq[0]])
      left += 1
    right += 1
  return solution

maxSlidingWindow([1,3,1,2,0,5], 3)
maxSlidingWindow([1,1,1,1,1,4,5], 6)
maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
maxSlidingWindow([1, -1], 1)
maxSlidingWindow([8,7,6,9], 2)