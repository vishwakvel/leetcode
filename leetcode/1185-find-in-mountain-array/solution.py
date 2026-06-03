# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        left = 0
        right = n - 1

        # find i
        while left < right:
            mid = (left + right) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        i = left

        #search left
        lleft = 0
        rleft = i
        while lleft <= rleft:
            mid = (lleft + rleft) // 2

            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                rleft = mid - 1
            else:
                lleft = mid + 1
        
        # search right
        rright = n - 1
        lright = i + 1

        while lright <= rright:
            mid = (rright + lright) // 2

            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                lright = mid + 1
            else:
                rright = mid - 1
        
        return -1
