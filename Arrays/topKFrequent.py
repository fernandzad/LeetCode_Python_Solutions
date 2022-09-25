def countAppaerances(nums):
  dictionary = dict()
  for x in nums:
    dictionary[x] = dictionary.get(x, 0) + 1
  return dictionary

def main(nums, k):
  dictionary = countAppaerances(nums)

  bucket = [[] for _ in range(len(nums) + 1)]

  for (key, value) in dictionary.items():
    bucket[value].append(key)
  
  solution = list()
  for array in reversed(bucket):
    if k == 0:
      break
    if len(array) > 0:
      for number in array:
        if k == 0:
          break
        solution.append(number)
        k -= 1
  return solution      


main([1, 1, 1, 2, 2, 3], 2)
main([1, 1, 1, 2, 2, 3], 3)
main([1, 1, 1, 2, 2, 3, 3, 3, 4], 2)
main([1], 1)