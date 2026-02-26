class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        elements=[item for sublist in grid for item in sublist]
        elements_=list(filter(lambda a: a<0,elements))
        return len(elements_)











        