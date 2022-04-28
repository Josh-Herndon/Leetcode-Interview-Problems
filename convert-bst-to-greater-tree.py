# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cur_sum = 0
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def convert(tree):
            if tree:
                convert(tree.right)
                self.cur_sum += tree.val
                tree.val = self.cur_sum
                convert(tree.left)
            
        convert(root)  
        return root
