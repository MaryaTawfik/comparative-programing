class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}
        for winner, loser in matches:
            if winner not in loss_count:
                loss_count[winner] = 0 
            if loser not in loss_count:
                loss_count[loser] = 0
            loss_count[loser] += 1  
        no_loss = []
        one_loss = []
        
        # Classify players based on their loss count
        for player, losses in loss_count.items():
            if losses == 0:
                no_loss.append(player)
            elif losses == 1:
                one_loss.append(player)
        
        # Sort the results for consistent output
        return [sorted(no_loss), sorted(one_loss)]



    