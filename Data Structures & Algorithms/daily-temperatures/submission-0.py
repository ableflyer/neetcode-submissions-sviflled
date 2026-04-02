class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        tl = len(temperatures)
        for i in range(tl):
            for j in range(i, tl):
                if temperatures[i] < temperatures[j]:
                    result.append(j-i)
                    break
                if j >= tl-1:
                    result.append(0)
        return result
