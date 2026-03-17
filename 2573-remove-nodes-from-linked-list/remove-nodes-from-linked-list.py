# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        demmy=ListNode(0)
        demmy.next=head
        temp=demmy
        stack=[]
        while temp :
            if not stack:
                stack.append(temp.val)
                temp=temp.next
            else:
                if temp.val > stack[-1]:
                    while temp  and  stack and temp.val > stack[-1]:
                        stack.pop()

                    stack.append(temp.val)
                    temp=temp.next
                else:
                    stack.append(temp.val)
                    temp=temp.next
        demmy=ListNode(0)
        cur=demmy
        for i in stack:
            cur.next=ListNode(i)
            cur=cur.next
        return demmy.next



        