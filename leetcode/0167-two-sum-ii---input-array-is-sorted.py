class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        1. Create left and right vars that keep track of indexes
        2. Go through list and compare the sum of numbers at the indexes
            a) If less, then because sorted, increase left index by 1
            b) If greater, then because sorted, decrease right index by 1
            c) If equal, return indexes as list
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr = numbers[left] + numbers[right]

            if curr == target:
                return [left+1, right+1]
            elif curr < target:
                left += 1
            else:
                right -= 1
