
def calculate_most_frequent(l, r, hash):
  most_frequent = 0
  length = (r - l) + 1
  for _, v in hash.items():
    if v > most_frequent:
      most_frequent = v
  difference = length - most_frequent
  return (length, difference)
    

def characterReplacement(s: str, k: int):
  l = 0
  hash = dict()
  for i in range(65, 65 + 26):
    hash[str(chr(i))] = 0
  mx = -(1 << 30)

  difference = 0
  for r in range(len(s)):
    hash[s[r]] += 1
    (length, difference) = calculate_most_frequent(l, r, hash)

    while difference > k:
      hash[s[l]] -= 1
      l += 1
      (length, difference) = calculate_most_frequent(l, r, hash)

    # print('dif: ' + str(difference), length)
    if difference <= k:
      if length > mx:
        mx = length
    
  return mx

print(characterReplacement("AABBB", 2)) # 5
print(characterReplacement("BAAAA", 2)) # 5
print(characterReplacement("ABAB", 2)) # 4
print(characterReplacement("AABAABBA", 1)) # 5
print(characterReplacement("ABAA", 0)) # 2