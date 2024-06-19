class Solution(object):
    def romanToInt(self, s):
        a = 0
        p = 0
        rs = s[::-1]
        r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in rs:
            if r[i] >= p:
                a += r[i]
            else:
                a -= r[i]
            p = r[i]
        return a
