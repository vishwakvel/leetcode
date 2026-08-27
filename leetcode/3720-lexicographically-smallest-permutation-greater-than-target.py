class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = defaultdict(int)

        for char in s:
            count[char] += 1
        
        for char in target:
            count[char] -= 1
        
        for i in range(len(target) - 1, -1, -1):
            curr = target[i]
            count[curr] += 1

            if any(x < 0 for x in count.values()):
                continue
            
            smallest = None

            for char in sorted(count):
                if char > curr and count[char] > 0:
                    smallest = char
                    break
            
            if smallest is None:
                continue
            
            count[smallest] -= 1
            ans = list(target[:i])
            ans.append(smallest)

            for char in sorted(count):
                ans.append(char * count[char])
            
            return "".join(ans)
        
        return ""