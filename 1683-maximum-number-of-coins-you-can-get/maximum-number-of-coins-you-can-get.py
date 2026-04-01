class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        l,r=0,len(piles)-1
        result=0
        piles.sort()
        while l<r:
            r-=1
            result+=piles[r]
            r-=1
            l+=1
        return result


        
        