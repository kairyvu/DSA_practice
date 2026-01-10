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

        def getTarget(l, r, increasing):
            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                if increasing:
                    if val < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if val < target:
                        r = mid - 1
                    else:
                        l = mid + 1
            return -1
        
        topMountain = getTopMountain()
        leftCheck = getTarget(0, topMountain, True)
        if leftCheck != -1:
            return leftCheck
        rightCheck = getTarget(topMountain + 1, length - 1, False)
        if rightCheck != - 1:
            return rightCheck
        return -1