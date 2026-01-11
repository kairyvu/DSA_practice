class Solution:
    def numOfWays(self, n: int) -> int:
        INT_LIMIT = 10**9 + 7
        twos = 6
        threes = 6

        for _ in range(2, n + 1):
            newTwos = (3 * twos + 2 * threes) % INT_LIMIT
            newThrees = (2 * twos + 2 * threes) % INT_LIMIT

            twos, threes = newTwos, newThrees
        return (twos + threes) % INT_LIMIT