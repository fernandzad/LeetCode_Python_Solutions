class Solution:
  def defangIPaddr(self, address: str) -> str:
    s = ""
    for c in address:
      if (c == '.'):
        s += str('[')
        s += str('.')
        s += str(']')
      else:
        s += str(c)
    return s