class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.segmentTree = [0] * 2*self.n
        for i in range(self.n):
            self.segmentTree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.segmentTree[i] = self.segmentTree[2*i] + self.segmentTree[2*i + 1]

    def update(self, index: int, val: int) -> None:
        treeIndex = index + self.n
        self.segmentTree[treeIndex] = val
        while treeIndex > 1:
            parentIndex = treeIndex // 2
            self.segmentTree[parentIndex] = self.segmentTree[treeIndex] + self.segmentTree[treeIndex ^ 1]
            treeIndex = parentIndex

    def sumRange(self, left: int, right: int) -> int:
        left, right = left + self.n, right + self.n
        res = 0
        while left <= right:
            if left & 1:
                res += self.segmentTree[left]
                left += 1
            if not (right & 1):
                res += self.segmentTree[right]
                right -= 1
            left //= 2
            right //= 2
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)