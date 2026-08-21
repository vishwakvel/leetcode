class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "{": "}", "[": "]"}

        for bracket in s:
            if bracket in pairs: # opening
                stack.append(bracket)
            else: # closing
                if not stack:
                    return False
                
                if pairs[stack.pop()] != bracket:
                    return False
        
        return not stack
