class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        
        def backtrack(curr, digits):
            if not digits:
                res.append(curr)
                return
            for c in phoneMap[digits[0]]:
                backtrack(curr + c, digits[1:])
        
        backtrack("", digits)
        return res