class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[]
        largest=heights[0]
        for i , val in enumerate(heights):
            if not stack:
                stack.append([i,val])
            # elif stack and stack[-1][1]>val:
            #     # newidx=stack[-1][0]
            newidx=i
            while stack and stack[-1][1]>=val:
                newidx=stack[-1][0]
                w=i-stack[-1][0]
                h=stack[-1][1]
                area=h*w
                largest=max(largest,area)
                stack.pop()
            stack.append([newidx,val])
        # print(stack)
        if  stack:
            for idx,val in stack:
                # print(largest)
                # print(w,val)
               
                w=len(heights)-idx
                area=w*val
                # print(val,idx)
                # print(largest)
                # print(area)
                largest=max(largest,area)
        return largest
        