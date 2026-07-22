class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            max_idx=i
            for j in range(i+1,len(names)):
                if heights[j]>heights[max_idx]:
                    max_idx=j

            heights[i],heights[max_idx]=heights[max_idx],heights[i]
            names[i],names[max_idx]=names[max_idx],names[i]
        return names