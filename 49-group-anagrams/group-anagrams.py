class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsmap = defaultdict(list)

        for s in strs:
            sortedStr = tuple(sorted(s))
            hsmap[sortedStr].append(s)
        return list(hsmap.values())