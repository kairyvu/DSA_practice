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

        def merge(a, b):
            res = []
            while a or b:
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res
            

        res = []
        for i in range(max(0, k - n), min(m, k) + 1):
            pick1 = maxSequence(nums1, i)
            pick2 = maxSequence(nums2, k - i)
            curr = merge(pick1, pick2)
            if res < curr:
                res = curr
        return res