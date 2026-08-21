class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        t = 0 # target pointer
        i = 1

        while t < len(target) and i < n+1:
            ans.append("Push")

            if target[t] != i:
                ans.append("Pop")
            else:
                t += 1
            
            i += 1
        
        return ans
