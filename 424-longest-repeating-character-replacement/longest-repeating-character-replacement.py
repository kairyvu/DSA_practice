class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l, maxFreq = 0, 0
        res = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            if freq[s[r]] > maxFreq:
                maxFreq = freq[s[r]]
            
            while r - l + 1 - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res