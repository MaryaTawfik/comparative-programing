class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score=sorted( score,reverse=True)
        rank=[]
        medals=[]
        for i in range(len(score)):
            if i==0:
                rank.append("Gold Medal")
            elif i==1:
                rank.append("Silver Medal")
            elif i==2:
                rank.append("Bronze Medal")
            else:
                rank.append(str(i+1))
        rank_dict = {rank[i]: sorted_score[i] for i in range(len(score))}
        for i in score:
            for key,value in rank_dict.items():
                if i==value:
                    medals.append(key)
        return medals

       

