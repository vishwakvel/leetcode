class MinStack:
    """
    1. Init: create 2 stacks, 1 for the values, and 1 for the current mins at the moment each value was added
    2. Push: add value to stack and then check if min_stack is empty
        a) If it is, then add val to it because it's the only number so it has to be the least
        b) If it isn't, then add the minimum of val and top of stack's min, since the top always stores the most recent min.
    3. Pop: Call .pop() on both stacks to remove the topmost element
    4. Top: Call stack[-1] to return the last element in list (aka the most recent addition to the stack since we're only adding using append)
    5. GetMin: Return the last element of the min_stack since it stores the most recent min value in the whole stack (this is done during push)
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
