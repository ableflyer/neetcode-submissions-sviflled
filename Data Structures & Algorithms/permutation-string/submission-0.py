from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        size = len(s1)

        window = Counter(s2[:size])

        if window == s1_count:
            return True
        
        for i in range(size, len(s2)):
            new = s2[i]
            old = s2[i-size]

            window[new] += 1

            window[old] -= 1
            if window[old] <= 0:
                del window[old]
            
            if window == s1_count:
                return True
        
        return False
