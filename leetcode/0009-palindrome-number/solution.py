class Solution(object):
    def isPalindrome(self, x):
        if (x<0):
            return False
        else:
            rx = int(str(x)[::-1])
            if (x-rx == 0):
                return True
            else:
                return False
