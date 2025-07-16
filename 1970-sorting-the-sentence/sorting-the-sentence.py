class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        new=[0]*len(words)
        for i in words:
            index=int(i[-1])
            new[index-1]=i[:-1]
           
        return " ".join(new)

         


        