class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        
        def maxSequence(nums, k):
            stack = []
            numOfPop = len(nums) - k
            
            for num in nums:
                while stack and stack[-1] < num and numOfPop > 0:
                    stack.pop()
                    numOfPop -= 1
                stack.append(num)
            return stack[:k]

        def merge(nums1, nums2):
            p1, p2 = 0, 0
            merged = []

            while p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1:] <= nums2[p2:]:
                    merged.append(nums2[p2])
                    p2 += 1
                else:
                    merged.append(nums1[p1])
                    p1 += 1
            
            merged.extend(nums1[p1:])
            merged.extend(nums2[p2:])
            return merged
            

        res = []
        for i in range(max(0, k - n), min(m, k) + 1):
            pick1 = maxSequence(nums1, i)
            pick2 = maxSequence(nums2, k - i)
            curr = merge(pick1, pick2)
            if res < curr:
                res = curr
        return res