class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        opraters={'+', '-', '*', '/'}
        for i in tokens:
            if i not in opraters:
                stack.append(i)
            else:
                x=int(stack[-2])
                y=int(stack[-1])

                if i == "+":
                    z = x + y
                elif i == "*":
                    z= x * y
                elif i == "-":
                    z=x-y
                else:
                    z=x/y
                stack.pop()
                stack.pop()
                stack.append(z)
        return int(stack[0])

        