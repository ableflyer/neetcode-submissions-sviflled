class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spe = [(position[i], speed[i]) for i in range(len(position))]
        pos_spe = sorted(pos_spe, key=lambda x:x[0], reverse=True)
        stack = []
        for i in range(len(pos_spe)):
            p, s = pos_spe[i]
            time = (target-p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
