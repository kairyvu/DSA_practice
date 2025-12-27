class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        bucketSize = valueDiff + 1

        def getBucket(val):
            return val // bucketSize
        
        for i, num in enumerate(nums):
            bucket = getBucket(num)
            if bucket in buckets:
                return True

            if (bucket - 1) in buckets and num - buckets[bucket - 1] <= valueDiff:
                return True
            if (bucket + 1) in buckets and buckets[bucket + 1] - num <= valueDiff:
                return True
            
            buckets[bucket] = num
            if i >= indexDiff:
                del buckets[getBucket(nums[i - indexDiff])]
        return False