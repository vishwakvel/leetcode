class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(left: int, right: int):
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True

        def backtrack(start: int, path: List[str]):
            if start == len(s):
                ans.append(path[:])
                return
            
            for i in range(start, len(s)):
                if isPalindrome(start, i):
                    path.append(s[start:i+1])
                    backtrack(i + 1, path)
                    path.pop()
            
        backtrack(0, [])
        return ans
