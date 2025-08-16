class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # new=[]
        # highest=[]
        # for i in range(len(score[0])):
        #     row=[]
        #     for j in range (len(score)):
        #         row.append(score[j][i])
        #     row.sort(reverse=True)
        #     highest.append(sum(row))
        #     maxv=highest[0]
        #     maxindex=0
        #     for i in range(len(highest)):
        #         if maxv<highest[i]:
        #             maxv=highest[i]
        #             maxindex=i
        # return maxindex
         #     new.append(row)
            
        # return highest
        for i in range (len(score)):
            for j in range (i+1,len(score)):
                if score[i][k]<score[j][k]:
                    score[i],score[j]=score[j],score[i]
        return score

        
                    

        


       
        
        