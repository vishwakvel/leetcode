class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def distance(x1: int, y1: int, x2: int, y2: int) -> float:
            return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

        x = sum(p[0] for p in positions) / len(positions) # centroid
        y = sum(p[1] for p in positions) / len(positions) # centroid

        for i in range(700):
            numerator_x = 0
            numerator_y = 0
            denominator = 0

            for px, py in positions:
                dist = distance(x, y, px, py)

                if dist == 0:
                    continue

                weight = 1 / dist

                numerator_x += px * weight
                numerator_y += py * weight
                denominator += weight
            
            if denominator == 0:
                break

            x = numerator_x / denominator
            y = numerator_y / denominator

        ans = 0

        for px, py in positions:
            ans += distance(x, y, px, py)

        return ans
