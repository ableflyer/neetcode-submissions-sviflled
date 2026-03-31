class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            counter = [0]*26
            for c in i:
                counter[ord(c) - ord('a')] += 1
            groups[tuple(counter)].append(i)
        return groups.values()