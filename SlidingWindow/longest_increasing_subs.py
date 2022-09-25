# 3. Longest Substring Without Repeating Characters
# Sliding Window + HashTable
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# O(n)

def lengthOfLongestSubstring(s: str):
  if len(s) == 0 or len(s) == 1:
    return len(s)
  
  # create vars
  l = 0
  char_set = set()
  count = 1
  mx = -(1 << 30)
  
  # Process the string
  for r in range(len(s)):
    # get rid of same char in set
    # move left forward
    while s[r] in char_set:
      char_set.discard(s[l])
      l += 1
      count -= 1
    # Update maximum
    if count > mx:
      mx = count
    # Move right and increase counter
    char_set.add(s[r])
    count += 1
  return mx


print(lengthOfLongestSubstring("abcabcda"))
print(lengthOfLongestSubstring("a"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("bbb"))