class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(char) for char in str(num)]
        count = [0] * 10

        for d in digits:
            count[d] += 1

        ans = []

        for d in digits:
            if d % 2 == 0:
                for x in (8, 6, 4, 2, 0):
                    if count[x]:
                        ans.append(str(x))
                        count[x] -= 1
                        break
            else:
                for x in (9, 7, 5, 3, 1):
                    if count[x]:
                        ans.append(str(x))
                        count[x] -= 1
                        break

        return int("".join(ans))
