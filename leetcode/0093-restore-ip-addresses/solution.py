class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def backtracking(path, index, dots):
            if dots == 4:
                if index == len(s):
                    ans.append(path[:-1])
                return
            
            for i in range(index, min(index+3, len(s))):
                segment = s[index:i+1]

                if len(segment) > 1 and segment[0] == "0" or int(segment) > 255:
                    break
                
                backtracking(path + segment + ".", i+1, dots+1)
        
        backtracking("", 0, 0)
        return ans
