
def LIS(nums, n):
  
  lis = [1 for i in range(n)]
  longest = 1
  
  for i in range(1, n):
    for j in range(0, i):
      if nums[i] > nums[j] and lis[i] < lis[j] + 1:
        lis[i] = lis[j] + 1
        longest = max(longest, lis[i])
  return longest

def main(tests): 
  while True:
    if tests == 0: 
      break
    n = int(input())
    nums = [0 for i in range(n)]
    for i in range(n):
      nums[i] = int(input())
    print(LIS(nums, n))
    tests -= 1
    
tests = int(input())
main(tests)
