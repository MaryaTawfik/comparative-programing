class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge=[]
        p1=0
        p2=0
        while word1 or word2:
            if word1 > word2:
                merge.append(word1[0])
                word1=word1[1:]
            else:
                merge.append(word2[p2])
                word2=word2[1:]
        return "".join(merge)

                
           
      
            


        