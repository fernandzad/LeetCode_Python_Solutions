changes = [50, 25, 10, 5, 1]
memo = [[-1 for i in range(10)] for j in range(10005)]

def dp(money, i):
  if memo[money][i] != -1:
    return memo[money][i]
  if money==0 or (money==0 and i==5):
    return 1
  if i >= 5:
    return 0
  if changes[i] > money:
      memo[money][i] = dp(money, i + 1)
      return memo[money][i]
  if changes[i] <= money:
    memo[money][i] = dp(money - changes[i], i) + dp(money, i + 1)
    return memo[money][i]


while True:
  money = int(input())   
  print(dp(money, 0))