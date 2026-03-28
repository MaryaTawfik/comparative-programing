class Solution:
    def isHappy(self, n: int) -> bool:
        # s=str(n)
        # if n == 1:
        #     return True
        # s=str(n)
        
        # elif n == 1:
        #     return True
        visited=set()
        while True:
            if n==1:
                return True
            if n in visited:
                return False
            total=0
            visited.add(n)
            s_= str(n)
            for i in s_:
                total+=int(i)**2
            n=total 
            # visited.add(n)
        # while n not in visited  :
        #     s=str(n)
           
        #     row=[]
        #     for i in s:
        #         row.append(int(i)**2)
                
        #     n=sum(row)
        #     if n==1:
        #         return True
        #     visited.add(n)
      
        # return False
        
        
            
        
       
        