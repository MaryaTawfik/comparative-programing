class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0 for _ in range(len(temperatures))]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                temp,idx=stack.pop()
                ans[idx]=i-idx
            stack.append([t,i])
        return ans

        