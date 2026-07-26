class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first = second = third = float("-inf")
        last = slast = float("inf")

        for n in nums:
            pfirst, psecond, plast = first, second, last

            first = max(first, n)
            second = max(second, min(pfirst, n))
            third = max(third, min(psecond, n))

            last = min(last, n)
            slast = min(slast, max(plast, n))

        return max(first * second * third, first * last * slast)
