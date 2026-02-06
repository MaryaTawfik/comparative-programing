class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minn=[]
        min=float('inf')
        if len(list1) < len(list2):
            x=list1
            y=list2
        else:
            x=list2
            y=list1
        for i in range (len(x)):
            if x[i] in y:
                if min> (x.index(x[i])+ y.index(x[i])):
                    min=x.index(x[i])+ y.index(x[i])
                    minn=[x[i]]
                elif min == (x.index(x[i])+ y.index(x[i])):
                    minn.append(x[i])
        return minn


                
           
      
                
        