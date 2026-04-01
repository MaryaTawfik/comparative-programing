class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # p1=0
        # p2=0
        # indx=-1
      
        # while p1<len(needle) and p2 <len(haystack):
        #     if haystck[p1]==needle[p2] and p2<len(needle):
        #         indx=p1
        #         while haystck[p1]==needle[p2]:
                
                    
        #             p1+=1
        #             p2+=1
        if not needle:
            return 0
        else:
            return haystack.find(needle)


            

       
        
        
