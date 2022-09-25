# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Graph - Bread First Search

import collections

def numIslands(grid):
  m = len(grid[0])
  n = len(grid)
  adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  queue = collections.deque()
  visited = [[0 for _ in range(m)] for _ in range(n)]

  def bfs(x, y, island):
    queue.append((x, y))
    visited[x][y] = island

    while len(queue) != 0:
      (top_x, top_y) = queue.pop()
      visited[top_x][top_y] = island

      for (a_x, a_y) in adjacents:
        n_x = top_x + a_x
        n_y = top_y + a_y
        if (
            n_x >= 0 and n_x < n and
            n_y >= 0 and n_y < m and
            grid[n_x][n_y] == '1' and
            visited[n_x][n_y] == 0
          ):
          queue.append((n_x, n_y))
          visited[n_x][n_y] = island
  count = 0
  for i in range(n):
    for j in range(m):
      if visited[i][j] == 0 and grid[i][j] == '1':
        count += 1
        bfs(i, j, count)
  print(count)
  return count

    
numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])