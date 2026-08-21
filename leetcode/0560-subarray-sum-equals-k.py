class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        currsum = 0
        ans = 0

        for num in nums:
            currsum += num

            if currsum - k in hashmap:
                ans += hashmap[currsum - k]

            hashmap[currsum] = hashmap.get(currsum, 0) + 1

        return ans
