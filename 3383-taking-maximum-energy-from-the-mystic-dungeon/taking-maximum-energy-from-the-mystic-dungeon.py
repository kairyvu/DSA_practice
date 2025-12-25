class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            nextJump = dp[i + k] if i + k < n else 0
            dp[i] = energy[i] + nextJump

        return max(dp)