from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        mapping=defaultdict(int)
        ans=[]


        for i in nums2:
            if not stack :
                stack.append(i)
            if i > stack[-1]:
                while stack and i > stack[-1] :
                    mapping[stack[-1]]=i
                    stack.pop()
                stack.append(i)
            else:
                stack.append(i)
        for i in stack:
            mapping[i]=-1
        for i in nums1:
            ans.append(mapping[i])
        return ans

        