class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tl = len(temperatures)
        result = [0] * tl
        stack = []
        if tl <= 1:
            return [0]
        for i in range(tl):
            if not stack:
                stack.append(i)
            elif temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    num = stack.pop()
                    result[num] = i-num
                stack.append(i)
            print(stack)
        return result
