class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1) > len(word2):
            shorter = word2
            longer = word1
        else:
            shorter = word1
            longer = word2
        
        ans = ""
        count = 0

        while count < len(shorter):
            ans += word1[count] + word2[count]
            count += 1
        
        ans += longer[count:]

        return ans
