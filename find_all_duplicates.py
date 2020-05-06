# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]
# for val in [num & (1<<n) for n in range(8)]:
#   print(val)
a = [4,3,2,7,8,2,3,1]
b = [5, 1, 1, 2, 3]
c = [4,3,2,4,8,2,3,8]
d = [10,2,5,10,9,1,1,4,3,7]
e = [13,8,5,3,20,12,3,20,5,16,9,19,12,11,13,19,11,1,10,2]

def findDuplicates(nums):
  n = len(nums) + 1
  ans = [0 for i in range(n)]
  for i,x in enumerate(nums):
    if ans[x] == -x:
      ans[x] *= -1 
    if ans[x] == 0:
      ans[x] = -x
  ans = [ item for i, item in enumerate(ans) if item > 0 ]
  return ans

print(findDuplicates(a))
print(findDuplicates(b))
print(findDuplicates(c))
print(findDuplicates(d))
print(findDuplicates(e))