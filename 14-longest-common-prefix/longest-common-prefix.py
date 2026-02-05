from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        res=[]
        p1,p2=0,0
        
        while p1<len(strs[0]) and p2<len(strs[-1]):
            if strs[0][p1]== strs[len(strs)-1][p2]:
                res.append(strs[0][p1])
                p1+=1
                p2+=1
            else:
                break 
        return "".join(res)
        