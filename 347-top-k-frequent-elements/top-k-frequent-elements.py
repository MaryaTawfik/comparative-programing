from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        sorted_sec_ele= sorted(counter.items(), key=lambda x:x[1],reverse=True)
        ans=[]
        p=0
        while len(ans)<k and p < len(sorted_sec_ele):
            ans.append(sorted_sec_ele[p][0])
            p+=1
        return ans

        