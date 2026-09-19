from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
       
        # need = Counter(t)
        # missing = len(t)  
        
        # left = start = end = 0
        # for right, char in enumerate(s, 1):  
        #     if need[char] > 0:
        #         missing -= 1
        #     need[char] -= 1
            
          
        #     if missing == 0:
                
        #         while left < right and need[s[left]] < 0:
        #             need[s[left]] += 1
        #             left += 1
               
        #         if end == 0 or right - left < end - start:
        #             start, end = left, right
               
        #         need[s[left]] += 1
        #         missing += 1
        #         left += 1
        
        # return s[start:end] 
    
        original=Counter(t)
        # {a:2}
        my_dict=defaultdict(int)
        # {a:2}
        l,r=0,0
        left,right=0,0
        min_=float(inf)
        required=len(original)
        # 2
        matched=0
        # m=1
        while l<=r and r<len(s):
            my_dict[s[r]]+=1
            if my_dict[s[r]] == original[s[r]]:
                matched+=1
                while matched == required:
                    if min_>r-l+1:
                        left=l
                        right=r
                        min_=r-l+1
                    my_dict[s[l]]-=1
                    if s[l] in original and original[s[l]] > my_dict[s[l]]:
                        matched -=1
                    l+=1
            r+=1

                
        if  right   == len(s):
            return s[left:]      
        elif min_ != float(inf):
            return s[left:right+1]
        return ""
        # return s[left:right+1] if min_ != float(inf) else ""

        



# {a:1,d:1,o:1,b:1,:e:1,c:1}
# origina={a:2,b:1,c:1}
# # "ADOBECODEBANC"
#    l     r

# l,r=0,0















