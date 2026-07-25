class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev = 0

        for log in logs:
            uid, typ, time = log.split(":")
            uid = int(uid)
            time = int(time)

            if typ == "start":
                if stack:
                    ans[stack[-1]] += time - prev

                stack.append(uid)
                prev = time
            else:
                ans[stack.pop()] += time - prev + 1
                prev = time + 1
        
        return ans
