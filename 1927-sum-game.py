class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        firsthalfquestions = 0
        secondhalfquestions = 0
        firsthalf = 0
        secondhalf = 0

        for index, char in enumerate(num):
            if index < n // 2:
                if char == "?":
                    firsthalfquestions += 1
                else:
                    firsthalf += int(char)
            else:
                if char == "?":
                    secondhalfquestions += 1
                else:
                    secondhalf += int(char)
                
        if (firsthalfquestions + secondhalfquestions) % 2 == 1: # odd questions means Alice can always cause imbalance
            return True
        
        if firsthalfquestions == secondhalfquestions: # questions cancel out
            return firsthalf != secondhalf
        
        return 2 * (firsthalf - secondhalf) != 9 * (secondhalfquestions - firsthalfquestions) 
        # check if diff is equal to how many 9 diff pairs that can be forced (alice and bob can always oppose each other's digit choices to form max diff of 9)