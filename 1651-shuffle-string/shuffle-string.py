class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=len(s)
        res=[0]*n
        for i in range(len(s)):
            position=indices[i]
            res[position]=s[i]
        return "".join(res)
        
        