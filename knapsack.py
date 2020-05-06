
values = [60, 10, 12]
weights = [40, 20, 30]
totalWeight = 50

n = len(values)

def knapSack(totalWeight, i): 
  if i == n or totalWeight <= 0: 
    return 0

  if weights[i] > totalWeight:
    return knapSack(totalWeight, i + 1) 

  else: 
    return max(knapSack(totalWeight - weights[i], i + 1) + values[i], knapSack(totalWeight, i + 1)) 

print(knapSack(totalWeight, 0))
