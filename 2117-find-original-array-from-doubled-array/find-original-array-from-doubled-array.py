from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed_counter = Counter(changed)
        original_array = []

        if len(changed) % 2 != 0:
            return []

        for key in sorted(changed):
            if key == 0 and changed_counter[key] % 2 == 1:
                return []
            if key * 2 in  changed_counter and key in     changed_counter:
                changed_counter[key] -= 1
                changed_counter[key*2] -= 1
                if changed_counter[key] <= 0:
                    del changed_counter[key]
                if changed_counter[key*2] <= 0:
                    del changed_counter[key*2]

                original_array.append(key)
          
            
            if len(original_array) == len(changed) // 2:
                return original_array

        return []




        # original=[]
        # changed_ = Counter(changed)

        # if len(changed)%2 != 0:
        #     return []
        # # [(1,1), (0,1), (3, 1), (6, 1)]
        # for x, value in sorted(changed_.items()):
           
        #     if x*2  in changed_:
        #         del changed_[x]
        #         del changed_[x*2]
        #         original.append(x)
        
        # return original if len(original) == len(changed) // 2 else []

        # changed.sort()
        # flag=False
        # for i in range(len(changed)):
        #     for j in range (i+1,len(changed)):
        #         if changed[j] == 2*changed[i]:
        #             changed.pop(j)
        #             break
        #     else:
        #         break
        # else:
        #     flag=True
        # if  flag :
        #     return changed
        # else:
        #     return []

        