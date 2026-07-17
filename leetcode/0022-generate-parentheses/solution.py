class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(path, closing, opening):
            if closing == n and opening == n:
                ans.append(path)
                return
            
            if closing < opening:
                backtrack(path + ")", closing+1, opening)
            
            if opening < n:
                backtrack(path + "(", closing, opening+1)
        
        backtrack("", 0, 0)
        return ans
