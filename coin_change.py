
changes = [50, 25, 10, 5, 1]

def dp(money, i): # State of the DP
  if money == 0 or (money == 0 and i == 5):
    return 1
  if i >= 5:
    return 0
  if changes[i] > money:
      return dp(money, i + 1)
  if changes[i] <= money:
    return dp(money - changes[i], i) + dp(money, i + 1)

while True:
  money = int(input())
  print(dp(money, 0))