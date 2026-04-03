class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans=[]
        for i in s:
            ans.append(ord(i)-97)
        prifix=[0]*(len(s)+1)
        for i ,j ,k in shifts:
            if k == 0:
                prifix[i]-=1
                prifix[j+1]+=1
            else:
                prifix[i]+=1
                prifix[j+1]-=1
        for i in range(1,len(prifix)):
            prifix[i]+=prifix[i-1]
        prifix2=prifix[:-1]
        res=[]
        for i in range(len(ans)):
            res.append((prifix2[i]+ans[i])%26)
        for i in range(len(res)):
            res[i]=chr(res[i]+97)
        return "".join(res)
