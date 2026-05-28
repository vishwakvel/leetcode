class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Convert nums to a counter
        2. Use counter's built in method most_common to get the k most common numbers
        3. Use a for loop to extract just the first element of each element in 2s output because most_common return not just the most common elements but also how many of each there are
        """
        
        from collections import Counter

        ans = []
        nums_counter = Counter(nums)

        for l in nums_counter.most_common(k):
            ans.append(l[0])

        return ans
