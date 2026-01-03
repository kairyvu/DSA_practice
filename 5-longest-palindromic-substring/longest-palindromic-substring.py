class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expandCenter(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        res = ""
        for i in range(n):
            odd = expandCenter(i,i)
            even = expandCenter(i,i+1)
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res