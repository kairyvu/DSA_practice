class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        INT_LIMIT = 10**9 + 7
        counterToRight = Counter(nums)
        counterToLeft = defaultdict(int)

        triplets = 0
        for num in nums:
            counterToRight[num] -= 1
            triplets += counterToLeft[num * 2] * counterToRight[num * 2]
            counterToLeft[num] += 1
        return triplets % INT_LIMIT