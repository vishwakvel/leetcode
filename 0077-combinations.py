class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(path, index, count):
            if count == k:
                ans.append(path.copy())
                return
            
            if count > k or index > n:
                return
            
            for i in range(index, n+1):
                path.append(i)
                backtrack(path, i+1, count+1)
                path.pop()
        
        backtrack([], 1, 0)
        return ans
