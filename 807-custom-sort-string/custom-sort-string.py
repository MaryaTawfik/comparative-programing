from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mapping=defaultdict(int)

        ans=[]
        s_=Counter(s)
        
        ans1=[]
        # print(ans)
       
        for i in  order:
            
            
            for j in range(s_[i]):
                    ans.append(i)
        for i in s_:
            if i not in order:
                for j in range(s_[i]):

                    ans.append(i)
        
        

            
                

        
        return "".join(ans)

        
        