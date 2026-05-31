from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # if len(p) > len(s):
        #     return -1
        target_counter=Counter(p)
        k=len(p)
        window_counter=Counter()
        result=[]

        if len(p) > len(s):
            return result

        for i in range(k):
            window_counter[s[i]]+=1

        if window_counter == target_counter:
            result.append(0)
        
        left=0

        for right in range(k,len(s)):
            window_counter[s[right]]+=1
            window_counter[s[left]]-=1

            if window_counter[s[left]] == 0:
                del window_counter[s[left]]
            
            if window_counter == target_counter:
                result.append(left+1)

            left+=1
        
        return result


       