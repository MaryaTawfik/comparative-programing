from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        arr=[]
        
        for i in strs:
            s=list(i)
            s.sort()
            row=[]
            row.append(s)
            row.append(i)
            arr.append(row)
        arr.sort()
        ans=[]
        p1=0
        while p1<len(arr):
            row=[]
            p2=p1
            while p2< len(arr) and arr[p2][0]==arr[p1][0]:
                row.append(arr[p2][1])
                p2+=1
           
            
            ans.append(row)
            p1=p2
            # print(row)
            row=[]
            
        return ans



            
        