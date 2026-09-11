class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10

        for digit in digits:
            count[digit] += 1
        
        ans = 0

        for i in range(1, 10):
            for j in range(10):
                for k in range(0, 10, 2):
                    if i == j == k:
                        if count[i] >= 3:
                            ans += 1
                    elif i == j:
                        if count[i] >= 2 and count[k] >= 1:
                            ans += 1
                    elif i == k:
                        if count[i] >= 2 and count[j] >= 1:
                            ans += 1
                    elif j == k:
                        if count[j] >= 2 and count[i] >= 1:
                            ans += 1
                    else:
                        if count[i] and count[j] and count[k]:
                            ans += 1

        return ans