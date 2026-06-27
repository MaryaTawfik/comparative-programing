class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0]*(len(s)+1)
        ans=list(s)

        for start,end,step in shifts:
            
            if step == 1:
                prefix_sum[start] += 1
                prefix_sum[end+ 1] -= 1
            else:
                prefix_sum[start] -= 1
                prefix_sum[end+1] += 1
        
        for i in range(1,len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]

        for c in range (len(s)):
            new=chr(((ord(s[c])-ord("a")) + prefix_sum[c]) % 26 + ord("a"))
            ans[c]=new
          

        
        return "".join(ans)

            




        