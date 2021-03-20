class Solution:
  def findCenter(self, edges) -> int:
    bucket = dict()

    for nodes in edges:
      v1 = nodes[0]
      v2 = nodes[1]
      bucket[v1] = 0
      bucket[v2] = 0
    for nodes in edges:
      v1 = nodes[0]
      v2 = nodes[1]
      bucket[v1] += 1
      bucket[v2] += 1
    
    numberEdges = len(edges)
    for key, val in bucket.items():
      if (val == numberEdges):
        return key

# Slower solution
# class Solution:
#   def findCenter(self, edges: List[List[int]]) -> int:
#     bucket = [0 for i in range(100002)]

#     for nodes in edges:
#       v1 = nodes[0]
#       v2 = nodes[1]
#       bucket[v1] += 1
#       bucket[v2] += 1
    
#     numberEdges = len(edges)
#     for nodes in edges:
#       v1 = nodes[0]
#       v2 = nodes[1]
#       if (bucket[v1] == numberEdges):
#         return v1
#       if (bucket[v2] == numberEdges):
#         return v2