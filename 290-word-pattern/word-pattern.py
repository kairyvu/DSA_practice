class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hsmap = {}
        lstStr = s.split()

        if len(pattern) != len(lstStr):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hsmap:
                hsmap[pattern[i]] = lstStr[i]
            elif hsmap[pattern[i]] != lstStr[i]:
                return False
        return len(hsmap) == len(set(lstStr))