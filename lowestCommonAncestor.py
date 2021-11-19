# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorder_traversal(tree, postorder_node_list=[]):
    if tree:
        postorder_traversal(tree.left, postorder_node_list)
        postorder_traversal(tree.right, postorder_node_list)
        postorder_node_list.append(tree)
        
    return postorder_node_list
        
def inorder_traversal(tree, inorder_node_list=[]):
    if tree:
        inorder_traversal(tree.left, inorder_node_list)
        inorder_node_list.append(tree)
        inorder_traversal(tree.right, inorder_node_list)
        
    return inorder_node_list
        
        
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         postorder_node_list = postorder_traversal(root)
#         inorder_node_list = inorder_traversal(root)
#         #print(postorder_node_list)
        
#         root_node = postorder_node_list[-1]
#         #print(root_node.val)
        
#         if len(postorder_node_list) <= 3:
#             return root_node.val
        
#         root_node_index = inorder_node_list.index(root_node)
        
#         left_subtree = inorder_node_list[:root_node_index]
#         right_subtree = inorder_node_list[root_node_index + 1:]
        
#         if p in left_subtree and q in left_subtree:
#             self.lowestCommonAncestor(root_node.left, p, q)
#         elif p in right_subtree and q in right_subtree:
#             self.lowestCommonAncestor(root_node.right, p, q)
#         else:
#             return root_node.val

def search(root, target, result=[]):
    if root:
        if root.left == target:
            result.append(root.left)
            return root.left
        elif root.right == target:
            result.append(root.right)
            return root.right
        else:
            if (root.left != None and type(search(root.left, target)) == TreeNode) or (root.right != None and type(search(root.right, target)) == TreeNode):
                return result[0]
            
        
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        p_path = [p]
        q_path = [q]

        node = root
        while root not in p_path:
            node = search(node, p)
            p_path.insert(0, node)
            if root.left == node or root.right == node:
                p_path.insert(0, root)
        
        node = root
        while root not in q_path:
            node = search(node, q)
            q_path.insert(0, node)
            if root.left == node or root.right == node:
                q_path.insert(0, root)

        i = 0
        while i < len(p_path) and i < len(q_path):
            if p_path[i] != q_path[i]:
                break
            i += 1
        
        return p_path[i-1].val

node_list = [3,5,1,6,2,0,8,None,None,7,4]
for i in range(len(node_list)):
    if node_list[i] != None:
        node_list[i] = TreeNode(node_list[i])

for i in range(len(node_list)//2):
    node_list[i].left = node_list[i*2 + 1]
    node_list[i].right = node_list[i*2 + 2]

s = Solution()
print(s.lowestCommonAncestor(node_list[0], node_list[4], node_list[9]))

#print(search(node_list[0], node_list[9]))