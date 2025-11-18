class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        n = len(heights)

        for i, h in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                startIndex = index
            stack.append((startIndex, h))
        
        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (n - index))
        return maxArea