from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mydict=defaultdict(list)
        for i in strs:
            s = sorted(list(i))
            
            mydict["".join(s)].append(i)
        ans=[]

        for val in mydict.values():
            ans.append(val)

        return ans

       