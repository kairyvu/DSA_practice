class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        INT_LIMIT = 10**9 + 7
        totalCount = Counter(nums)
        counterToLeft = defaultdict(int)
        if 0 in totalCount:
            totalCount[0] -= 1

        triplets = 0
        for num in nums:
            leftCount = counterToLeft[num * 2] 
            triplets += leftCount * (totalCount[num * 2] - leftCount)
            counterToLeft[num] += 1
        return triplets % INT_LIMIT