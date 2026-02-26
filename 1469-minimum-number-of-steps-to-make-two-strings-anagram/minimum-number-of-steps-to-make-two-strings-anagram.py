from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count=0
        s_counter=Counter(s)
        t_counter=Counter(t)
        s_=set(s)
        for i in s_:
            if i not in t_counter:
                count=count+s_counter[i]
            elif s_counter[i] >t_counter[i]:
                diff =s_counter[i] - t_counter[i]
                
                count=count+diff
        return count


        
        