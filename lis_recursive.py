# arr = [2, 5, 3]
# arr = [2, 5, 3, 1, 2, 3, 4]
# arr = [2, 5, 3, 1, 2, 3]
arr = [1, 6, 2, 3, 5]
n = len(arr)

def lis(n, longest):
  # Base case 
  if n == 1:
    return 1

  # 'max_ending_here' is length of LIS ending with arr[n-1] 
  max_ending_here = 1

  for i in range(1, n):
    res = lis(i, longest)
    if arr[i - 1] < arr[n - 1] and res + 1 > max_ending_here:
      max_ending_here = res + 1
      
  # Compare max_ending_here with the overall max. And 
  # update the overall max if needed 
  if longest < max_ending_here: 
    longest = max_ending_here 

  # Return length of LIS ending with arr[n-1] 
  return max_ending_here 

print(lis(n, 1))