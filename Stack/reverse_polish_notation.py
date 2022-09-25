# 150. Evaluate Reverse Polish Notation
# Solved with a Stack
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

def evalRPN(tokens):
  stack = []

  def operate(stack, operator):
    val2 = stack.pop()
    val1 = stack.pop()
    number1 = int(val1)
    number2 = int(val2)
    if operator == '*':
      result = number1 * number2
    elif operator == '+':
      result = number1 + number2
    elif operator == '-':
      result = number1 - number2
    elif operator == '/':
      result = int(number1 / number2)
    return str(result)

  for c in tokens:
    if c == '*' or c == '/' or c == '+' or c == '-':
        result = operate(stack, c)
        stack.append(result)
    else:
      number = int(c)
      stack.append(number)
  print(stack)

evalRPN(["2","1","+","3","*"])
evalRPN(["4","13","5","/","+"])
evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])