# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node):
            if node:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                
                traverse(node.left)
                traverse(node.right)
                
        traverse(root)
        
        return root
