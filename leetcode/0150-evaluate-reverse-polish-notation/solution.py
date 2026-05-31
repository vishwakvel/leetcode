class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Postfix to infix conversion
        1. 
        """
        stack = []

        for token in tokens:            
            if token in "+-*/":
                second = int(stack.pop())
                first = int(stack.pop())

                if token == "+":
                    stack.append(first+second)
                elif token == "-":
                    stack.append(first-second)
                elif token == "*":
                    stack.append(first*second)
                else:
                    stack.append(int(first/second))
            else:
                stack.append(int(token))
        
        return stack.pop()
