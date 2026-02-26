from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq_s= Counter(s).items()
        #[(t,1),(r,1),(e,2)]
        freq_ss=sorted(freq_s, key= lambda a:a[1] , reverse= True)
        res=[]
        for key , val in freq_ss:
            res.append(key*val)
        return "".join(res)

        # for key,val in sort(freq_s.items()):
        #     for i in range (val):
        #         res.append(key)
        # ans = "".join(res)
        # return ans


        