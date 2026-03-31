class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        count = sorted(count.items(), key=lambda x: x[1])
        print(count)
        keys = [i[0] for i in count]
        return keys[len(keys)-k:]