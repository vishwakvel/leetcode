class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        num = 0

        for char in s:
            if char in "0123456789":
                num = num * 10 + int(char)
            elif char in "+-":
                result += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += sign * num
                num = 0

                sign = stack.pop()
                prev = stack.pop()

                result = prev + sign * result
            else:
                continue

        return result + sign * num
