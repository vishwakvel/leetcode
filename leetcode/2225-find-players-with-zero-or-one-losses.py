class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {} # player id to count
    
        for winner, loser in matches:
            losses[winner] = losses.get(winner, 0)
            losses[loser] = losses.get(loser, 0) + 1
        
        none = []
        one = []

        for player in sorted(losses):
            if not losses[player]:
                none.append(player)
            elif losses[player] == 1:
                one.append(player)
        
        return [none, one]