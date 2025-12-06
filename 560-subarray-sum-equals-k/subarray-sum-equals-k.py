class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hsmap = defaultdict(int)
        hsmap[0] = 1
        currSum, res = 0, 0

        for num in nums:
            currSum += num
            res += hsmap[currSum - k]
            hsmap[currSum] += 1
        return res