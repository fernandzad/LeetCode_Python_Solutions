# 347. Top K Frequent Elements
# link: https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(nums, k):
  repetitions = {}
  for n in nums:
    repetitions[n] = repetitions.get(n, 0) + 1
  bucket = [[] for _ in range(len(nums) + 1)]
  for i, v in repetitions.items():
    bucket[v].append(i)

  solution = []
  for nums in reversed(bucket):
    if k == 0:
      break
    idx = 0
    while idx < len(nums):
      if k == 0:
        break
      solution.append(nums[idx])
      k -= 1
      idx += 1
  return solution
  print(solution)

topKFrequent([1], 1)
topKFrequent([1,1,1,2,2,3], 2)
topKFrequent([1,1,1,2,2,2,3], 1)
topKFrequent([1,1,1,2,2,2,3,3,3], 3)
topKFrequent([-1,-1,-1,2,2,-3,-3,-3], 2)
topKFrequent([1,1,1,1,1,1], 1)
#           0,1,2,3,4,5, 6 
# bucket = [            [1]  ]