from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ops = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b,
            "*": lambda a,b: a * b,
            "/": lambda a,b: int(a / b) 
        }
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                res = ops[i](a,b)
                stack.append(res)
        return stack[0]
            