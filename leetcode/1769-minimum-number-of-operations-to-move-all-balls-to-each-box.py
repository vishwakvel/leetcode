class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        moves = 0
        balls = 0

        for i in range(n):
            ans[i] += moves
            balls += 1 if boxes[i] == "1" else 0
            moves += balls
        
        balls = 0
        moves = 0

        for i in range(n - 1, -1, -1):
            ans[i] += moves
            balls += 1 if boxes[i] == "1" else 0
            moves += balls

        return ans