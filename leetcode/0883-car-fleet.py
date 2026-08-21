class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        1. Create a cars list that contains tuples of position and speeds of cars. Then sort the list in reverse so you have the closest positions first, then the furthest. Then create an empty stack which will be how you track the unique times.
        2. Iterate through cars and for each car, calculate the time it takes to reach target. Then check if the stack is empty or if the time the current car takes is greater than the previous unique time a car took (aka if it can or cannot catch up so it needs its own fleet)
            a) If either condition is true, then either we're looking at the first car so we just add since there's no other fleets or cars we've looked at. Also, if the time is greater, that means this car takes longer to reach the target, so there's no way it can catch up to any cars ahead of it, and thus needs its own fleet. So, we add the time to the stack.
            b) If false, then continue
        3. We finally return the length of the stack (aka the number of unique times the cars take to reach the target)
        """
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
