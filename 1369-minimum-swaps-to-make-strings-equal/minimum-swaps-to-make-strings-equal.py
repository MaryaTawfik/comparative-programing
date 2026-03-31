class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        sx=0
        sy=0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            elif s1[i] == "x" and s2[i] == "y" :
                sx+=1
            elif s1[i] == "y" and s2[i] =="x":
                sy+=1
        if (sx+sy) %2 != 0:
            return -1
        swap=(sx//2 + sy//2)
        if sx%2!=0:
            return swap+2
        return swap


            
        