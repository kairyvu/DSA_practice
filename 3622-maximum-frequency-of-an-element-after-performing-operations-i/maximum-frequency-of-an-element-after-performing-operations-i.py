class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        count = Counter(nums)
        freq = defaultdict(int)
        points = set()

        for num in nums:
            leftBound = num - k
            rightBound = num + k + 1
            freq[leftBound] += 1
            freq[rightBound] -= 1

            points.add(leftBound)
            points.add(rightBound)
            points.add(num)

        res = 0
        curr = 0
        for p in sorted(points):
            curr += freq[p]
            existingNum = count[p]
            res = max(res, existingNum + min(numOperations, curr - existingNum))
        return res