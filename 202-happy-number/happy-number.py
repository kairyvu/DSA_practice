class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        currSum = n
        while currSum != 1:
            n = currSum
            currSum = 0
            while n > 0:
                digit = n % 10
                currSum += digit**2
                n //= 10
            if currSum in visited:
                return False
            visited.add(currSum)
        return True