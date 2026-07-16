class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []

        def binarysearch(arr, n):
            left = 0
            right = len(arr) - 1

            while left < right:
                mid = (left + right) // 2

                if n == arr[mid]:
                    return mid
                elif n > arr[mid]:
                    left = mid + 1
                else:
                    right = mid
                
            return left

        for num in nums:
            if not ans or num > ans[-1]:
                ans.append(num)
            else:
                i = binarysearch(ans, num)
                ans[i] = num
        
        return len(ans)
