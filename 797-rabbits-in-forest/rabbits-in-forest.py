from collections import Counter
import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans=Counter(answers)
        res=0
        for i in ans:
            colors= math.ceil(ans[i]/(i+1))*(i+1)
            res+=colors
        return res

        # ans=set(answers)
        # res=0
        # #1,2
        # for i in ans:
        #     res+=i
        # return res+len(answers)
        