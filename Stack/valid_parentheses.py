# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Stack every open parentheses, if stack empty is true!


def isValid(s: str):
  stack = []
  for c in s:
    if c == '(' or c == '{' or c == '[':
      stack.append(c)
    else:
      if len(stack) >= 1:
        top = stack[-1]
        if (c == ')' and top == '(') or (c == ']' and top == '[') or (c == '}' and top == '{'):
          stack.pop()
        elif c == '}' or c == ']' or c == ')':
          stack.append(c)
      elif c == '}' or c == ']' or c == ')':
        stack.append(c)

  return True if len(stack) == 0 else False
print(isValid('[()]'))
print(isValid('[(}]'))
print(isValid(']'))
print(isValid(']()[]'))
print(isValid('(})'))