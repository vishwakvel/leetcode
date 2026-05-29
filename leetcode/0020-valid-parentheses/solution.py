class Solution:
    def isValid(self, s: str) -> bool:
        """
        1. Create an empty stack (use stack because parenthesis have highest priority so once a close paren char is found the stack has to contain the open paren to properly complete the pair)
        2. Create a pairs dict assigning the closing chars to the opening chars
        3. Loop through each char in s and check if char is either opening or closing
            a) If opening, then add to stack
            b) If closing, then check if stack is either empty or if the top of the stack is the relative opening char
                a) If empty or not the relative opening char then return False
                b) If not, then continue
        4. Check if stack is empty
            a) If it is, then all chars have been taken care of and the parenthesis pairings were done properly. Return True
            b) If it isnt, then False because there's leftover chars that weren't assigned properly
        """
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or stack.pop() != pairs[char]:
                    return False
        
        return len(stack) == 0
