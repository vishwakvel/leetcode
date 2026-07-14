class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def dp(expr):
            if expr in memo:
                return memo[expr]
            
            res = []

            for i, char in enumerate(expr):
                if char in "+-*":
                    left = dp(expr[:i])
                    right = dp(expr[i+1:])

                    for a in left:
                        for b in right:
                            if char == "+":
                                res.append(a + b)
                            elif char == "-":
                                res.append(a - b)
                            else:
                                res.append(a * b)
                    
            
            if not res:
                res.append(int(expr))

            memo[expr] = res
            return res

        return dp(expression)
