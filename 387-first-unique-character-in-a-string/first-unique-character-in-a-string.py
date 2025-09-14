class Solution:
    def firstUniqChar(self, s: str) -> int:
        # l,r=0,len(s)-1
        # while l<=r:
        #     while r>=l and s[l]!=s[r]:
        #         r-=1
        #     return l
           
        #     l,r=l+1,r-1
        # return -1
        from collections import Counter
        c=Counter(s)
        for i in range (len(s)):
            if c[s[i]]==1:
                return i
        return -1


        