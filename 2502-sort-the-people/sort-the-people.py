class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:



        # m=[]
        d=list(zip(heights,names))
        for i in range(len(d)-1):
            for j in range(0,len(d)-i-1):
                if d[j][0]<d[j+1][0]:
                    d[j],d[j+1] = d[j+1],d[j]
        return [name for value , name in d]
        # print(d)
        # k=list(d.keys())
        # k.sort(reverse=True) 
        # for i in k:
        #     m.append(d[i])
        # return m

       

        