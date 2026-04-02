from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {")": "(", "]":"[", "}": "{"}
        for i in s:
            if i in mapping.values():
                stack.append(i)
            else:
                if not stack or stack.pop() != mapping[i]:
                    return False
        return not stack