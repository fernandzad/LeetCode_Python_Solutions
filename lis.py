# Input  : arr[] = {3, 10, 2, 1, 20}
# Output : Length of LIS = 3
# The longest increasing subsequence is 3, 10, 20

# Input  : arr[] = {3, 2}
# Output : Length of LIS = 1
# The longest increasing subsequences are {3} and {2}

# Input : arr[] = {50, 3, 10, 7, 40, 80}
# Output : Length of LIS = 4
# The longest increasing subsequence is {3, 7, 40, 80}

a = [3, 10, 2, 1, 20]
n = len(a)


# i is previous position and j is current position
def lis(i, j):
  if i >= n or j >= n:
    return 0
  
  if i < 0 and a[j] > a[i]:
    took = 1 + lis(j, j + 1)
  
  notTook = lis(i, j + 1)
  # print(took, notTook)
  return max(took, notTook)

print (lis(-1, 0))