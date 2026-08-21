class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        ans = []

        def backtrack(path, index):
            if index == len(digits):
                ans.append(path)
                return
            
            if digits[index] not in letters:
                return
            
            for letter in letters[digits[index]]:
                path += letter
                backtrack(path, index+1)
                path = path[:len(path)-1]
        
        backtrack("", 0)
        return ans
