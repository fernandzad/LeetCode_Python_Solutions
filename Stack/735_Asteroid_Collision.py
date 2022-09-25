class Solution:
  def asteroidCollision(self, asteroids):
    solution = list()
    stack = []
    for asteroid in asteroids:
      if asteroid > 0:
        stack.append(asteroid)
      else:
        if not stack:
          solution.append(asteroid)
        while stack:
          abs_asteroid = abs(asteroid)
          if abs_asteroid > stack[-1]:
            stack.pop()
          elif abs_asteroid == stack[-1]:
            stack.pop()
            break
          else:
            break
          if not stack:
            solution.append(asteroid)
    solution.extend(stack)
    return solution