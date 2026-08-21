class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtracking(path, visited):
            if len(path) == len(nums):
                ans.append(path.copy())
                return

            for i in range(len(nums)):
                if i in visited:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and i-1 not in visited:
                    continue
                    
                visited.add(i)
                path.append(nums[i])
                backtracking(path, visited)
                path.pop()
                visited.remove(i)
        
        backtracking([], set())
        return ans
