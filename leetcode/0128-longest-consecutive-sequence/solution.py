class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        1. Convert to set to remove duplicates
        2. Go through each number in the set
        3. Check if theres a number right before it thats already in the set
            a) If there is, then skip the current number because it will already be checked by the number previous
            b) If there isn't, then set length = 1 and then increment length by 1 for each num+length (length changes by 1 every time so it looks at consecutive elements). Longest is also set to the max of the current length and the previous longest, thus making sure the longest sequence is stored and not the most current
        4. Return longest
        """
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1

                while num + length in nums_set:
                    length += 1
                
                longest = max(longest, length)
        
        return longest
