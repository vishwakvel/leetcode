class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even = 0
        odd = 0
        smallest = None

        for num in nums1:
            if not smallest:
                smallest = num
            
            smallest = min(smallest, num)

            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        
        if not odd or not even or smallest % 2 == 1:
            return True
        
        return False