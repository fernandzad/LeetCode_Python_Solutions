# 242. Valid Anagram
# HashMap, ArrayHashMap
# https://leetcode.com/problems/valid-anagram/
# O(n)

def isAnagram(s: str, t: str):
  if len(s) != len(t):
    return False
  anagram = [0 for i in range(27)]
  anagram2 = [0 for i in range(27)]
  
  for i in range(len(s)):
    anagram[ord(s[i]) - ord('a')] += 1
    anagram2[ord(t[i]) - ord('a')] += 1

  for i in range(27):
    if anagram[i] != anagram2[i]:
      return False
  return True
