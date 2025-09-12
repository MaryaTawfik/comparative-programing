class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # print(s.reverse())
        n=len(s)-1
        i=0
        while n>i:
            s[i],s[n]=s[n],s[i]
           

            i=i+1
            n=n-1
        return s
        # s[:]=s[::-1]
        # return s
