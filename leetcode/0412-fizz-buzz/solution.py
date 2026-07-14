class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(n):
            if (i+1) % 15 == 0:
                answer.append("FizzBuzz")
            elif (i+1) % 5 == 0:
                answer.append("Buzz")
            elif (i+1) % 3 == 0:
                answer.append("Fizz")
            else:
                answer.append(str(i+1))
        
        return answer
