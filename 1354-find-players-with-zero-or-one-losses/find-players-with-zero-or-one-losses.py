from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=[]
        loosers=[]
        answ=set()
        ansl=set()
        ans=[]
        for i ,j in matches:
            winners.append(i)
            loosers.append(j)
        
        counter_looser = Counter(loosers)
        
        

        for i in range(len(loosers)):
            if counter_looser[loosers[i]] == 1:
                ansl.add(loosers[i])
        
        for j in winners:
            if j not in counter_looser:
                answ.add(j)
        ans_=list(answ)
        ans__=list(ansl)
        ans_.sort()
        ans__.sort()
        ans.append(ans_)
        ans.append(ans__)
        return(ans)

        

        
    

            
        
        