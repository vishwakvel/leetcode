class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        1. Create an empty increasing order stack (so smallest closest to 0 and largest furthest), set to keep track of letters we've seen already, and a Counter to keep track of modes for each letter and make sure we always account for all the letters
        2. For each char in s, we first subtract 1 from its value in Counter. Then we check if we've already seen the character before
            a) If we have, then we skip this char completely
            b) If we haven't we continue
        3. We then check if the stack isn't empty, if the current character is smaller, and if the count of the last letter in the stack is greater than 0
            a) If all statements are true, then we can pop the stack and remove that char from seen because we can confidently say that there's more of that char later on in s and also because the current char needs to come before the last element in the stack since this is an increasing stack
            b) If any are false, then continue
        4. Add the char to the stack and seen set and finally return the the set as a string
        """
        stack = []
        seen = set()
        count = Counter(s)

        for char in s:
            count[char] -= 1

            if char in seen:
                continue

            while stack and char < stack[-1] and count[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)
        
        return "".join(stack)
