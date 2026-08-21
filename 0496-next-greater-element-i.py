class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                greater[stack.pop()] = num
            
            stack.append(num)
        
        while stack:
            greater[stack.pop()] = -1
        
        return [greater[n] for n in nums1]
