class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in image:
            # print(i)
            rev=i[::-1]
            row=[]
            # print(rev)
           
            for j in rev:
                
                if j == 0:
                    row.append(1)
                else:
                    row.append(0)
            # print(row)
            ans.append(row)
        return ans
        


        