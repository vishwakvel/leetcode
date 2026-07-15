class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(path, opencount, closecount):
            if opencount == n and closecount == n:
                ans.append(path)
                return
            
            if opencount < n:
                backtrack(path + "(", opencount+1, closecount)

            if closecount < opencount:
                backtrack(path + ")", opencount, closecount+1)
        
        backtrack("", 0, 0)
        return ans
