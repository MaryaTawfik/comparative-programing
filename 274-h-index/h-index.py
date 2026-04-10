class Solution:
    def hIndex(self, citations: List[int]) -> int:
        paper=[0]*(len(citations)+1)
        n=len(citations)
        for c in citations:
            paper[min(c,n)]+=1
        h=n
        papers=paper[n]
        while papers<h:
            h-=1
            papers+=paper[h]
        return h
