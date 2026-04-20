from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.doc = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.doc[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.doc:
            return ""
        
        arr = self.doc[key]
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r)//2
            if arr[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid
        
        if l <= 0:
            return ""
        
        return arr[l - 1][0]
