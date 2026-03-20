# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        #start from the root
        sum=0
        if not root:
            return 0
        if root.val%2==0:
            if root.left :
                if root.left.left:
                    sum+=root.left.left.val
                if root.left.right:
                    sum+=root.left.right.val
            if root.right :
                if root.right.left:
                    sum+=root.right.left.val
                if root.right.right:
                    sum+=root.right.right.val
        left_sum= self.sumEvenGrandparent(root.left)
        right_sum= self.sumEvenGrandparent(root.right)
        return sum+left_sum+right_sum
        
        #if root.val%2==0
        
            #cheack the left sub tree
                #if left.root and left.root.root
                    #sum+value
                #if left.root and root.left.right
                    #sum+value

                # we apply the same thing for the right sub tree 
        #we call the recurssion for  root.left
        #we call the recurssion for  root.rigt

        