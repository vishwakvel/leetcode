class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        1. Create answer list with same length as temperatures and default value as 0. Also create an empty stack (we will make sure this is descending only)
        2. For each temp in the list, check if first that the stack isn't empty (basically to skip the first element since there isn't anything previously in the stack) and then if the new element being added is greater than the least element in temperatures
            a) If it is, then we remove it from the stack and set answer[removed value] to be the difference between the current index just added and the index of the removed value. We loop this until it fails
            b) If it isn't, then continue
        3. We add the new index to the stack
        """
        answer = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j
            
            stack.append(i)
        
        return answer
