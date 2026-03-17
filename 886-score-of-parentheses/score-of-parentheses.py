class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        top=0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(0)
            else:
                top=stack.pop()
                topp =1 if top ==0 else 2*top
                stack[-1]+=topp
        return stack[0]


        
      
            