# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        def getTopMountain():
            l, r = 0, length - 1
            while l < r:
                mid = (l + r) // 2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    l = mid + 1
                else:
                    r = mid
            return l

        def getTargetLeft(topMountain):
            l, r = 0, topMountain
            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        def getTargetRight(topMountain):
            l, r = topMountain, length - 1
            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        topMountain = getTopMountain()
        leftCheck = getTargetLeft(topMountain)
        if leftCheck != -1:
            return leftCheck
        rightCheck = getTargetRight(topMountain + 1)
        if rightCheck != - 1:
            return rightCheck
        return -1