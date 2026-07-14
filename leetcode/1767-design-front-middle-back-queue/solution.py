from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)

        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())

        self.left.append(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)

        if len(self.right) > len(self.left):
            self.left.append(self.right.popleft())

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1

        ans = self.left.popleft()

        if len(self.right) > len(self.left):
            self.left.append(self.right.popleft())
        
        return ans

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1

        ans = self.left.pop()

        if len(self.right) > len(self.left):
            self.left.append(self.right.popleft())
        
        return ans

    def popBack(self) -> int:
        if not self.left and not self.right:
            return -1

        if self.right:
            ans = self.right.pop()
        else:
            ans = self.left.pop()

        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        
        return ans

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
