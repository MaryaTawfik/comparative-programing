class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        m=[]
        d=dict(zip(heights,names))
        k=list(d.keys())
        k.sort(reverse=True) 
        for i in k:
            m.append(d[i])
        return m

       

        