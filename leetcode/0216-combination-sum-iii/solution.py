class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def backtracking(path, total, index, count):
            if total == n:
                if count == k:
                    ans.append(path.copy())
                    return
            
            if total > n or count >= k:
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtracking(path, total+nums[i], i+1, count+1)
                path.pop()
            
        backtracking([], 0, 0, 0)
        return ans
