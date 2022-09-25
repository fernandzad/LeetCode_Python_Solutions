# 49. Group Anagrams
# Sorting/HashMap
# https://leetcode.com/problems/group-anagrams/
# O(m * nlogn)

# strs is list of string -> list of lists of strings
def groupAnagrams(strs):
  hash = dict()
  solu = []
  for s in strs:
    s_sorted = ''.join(sorted(s))
    # key: aet
    if hash.get(s_sorted, False) == False:
      hash[s_sorted] = []
      hash[s_sorted].append(s)
    else:
      hash[s_sorted].append(s)
  for values in hash.values():
    solu.append(values)
  return solu

groupAnagrams(["eat","tea","tan","ate","nat","bat"])

# eat = aet
# tea = aet
# ate = aet
# tan = ant
"""
  hash = {
    "ate": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"]
  }
"""