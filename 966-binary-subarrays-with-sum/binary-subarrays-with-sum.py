class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        preSum = 0
        res = 0
        
        for num in nums:
            preSum += num
            res += count[preSum - goal]
            count[preSum] += 1
        return res