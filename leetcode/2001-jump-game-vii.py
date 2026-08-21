class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        left = 0
        count = 0
        dp = [False] * len(s)
        dp[0] = True

        for right in range(1, len(s)):
            if right - minJump >= 0 and dp[right - minJump]:
                count += 1
            
            if right - maxJump - 1 >= 0 and dp[right - maxJump - 1]:
                count -= 1
            
            if count > 0 and s[right] == "0":
                dp[right] = True

                if right == len(s) - 1:
                    return True
            
        return False
