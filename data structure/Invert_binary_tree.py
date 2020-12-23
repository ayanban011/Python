# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object): 
    def invertTree(self, root):
        l=[]
        if (root == None): 
            return
        temp = root
        Solution.invertTree(self,root.left)
        Solution.invertTree(self,root.right)
        temp = root.left  
        root.left = root.right  
        root.right = temp 
        return root
