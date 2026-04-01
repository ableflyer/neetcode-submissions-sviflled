class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            first = s[i].lower()
            last = s[j].lower()
            if not last.isalnum():
                j -= 1
            elif not first.isalnum():
                i += 1
            else:
                if first != last:
                    return False
                i += 1
                j -= 1
        return True