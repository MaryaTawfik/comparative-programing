from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        visited={}
        
        min_len= float('inf')
        current_len=0

        if len(cards)==len(set(cards)):
            return -1

        for right in range(len(cards)):
            if cards[right] in visited:
                left=visited[cards[right]]
                current_len=right-left+1
                min_len=min(min_len,current_len)
                
            visited[cards[right]]=right
        return min_len