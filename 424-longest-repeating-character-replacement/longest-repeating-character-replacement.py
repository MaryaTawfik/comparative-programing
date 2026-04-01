class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        max_=0
        counter_dict={}
        for r in range(len(s)):
            if  not s[r]  in counter_dict:
                counter_dict[s[r]] = 0
            counter_dict[s[r]]+=1
            if (r-l+1 )- max(counter_dict.values())<=k:
                max_=max(max_,r-l+1)
            else:
                counter_dict[s[l]]-=1
                if not counter_dict[s[l]]:
                    counter_dict.pop(s[l])
                l+=1
        return max_
        
        