class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hsmap = {}

        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            
            hsmap[nums2[i]] = -1 if not stack else stack[-1]
            stack.append(nums2[i])
        
        res = []
        for i in range(len(nums1)):
            res.append(hsmap[nums1[i]])
        return res