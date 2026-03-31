class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_set = {}
        t_set = {}
        for i in range(len(s)):
            cur_s = s[i]
            cur_t = t[i]
            if cur_s in s_set:
                s_set[cur_s] += 1
            else:
                s_set[cur_s] = 1
            
            if cur_t in t_set:
                t_set[cur_t] += 1
            else:
                t_set[cur_t] = 1
        if s_set == t_set:
            return True
        return False