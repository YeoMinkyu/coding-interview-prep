# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            root = TreeNode(val)
        else:
            self._insert_value(root, val)
        
        return root

    def _insert_value(self, root: Optional[TreeNode], val: int) -> None:
        
        if val < root.val:
            if root.left:
                self._insert_value(root.left, val)
            else:
                root.left = TreeNode(val)
                return
        else:
            if root.right:
                self._insert_value(root.right, val)
            else:
                root.right = TreeNode(val)
                return


# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if root is None:
#             root = TreeNode(val)
#         elif val > root.val:
#             self.insert_after(root, val)
#         else:
#             self.insert_before(root, val)
        
#         return root

#     def insert_after(self, node, val):
#         if node.right is None:
#             node.right = TreeNode(val)
#             return
#         else:
#             if val > node.right.val:
#                 self.insert_after(node.right, val)
#             else:
#                 self.insert_before(node.right, val)

#     def insert_before(self, node, val):
#         if node.left is None:
#             node.left = TreeNode(val)
#             return
#         else:
#             if val > node.left.val:
#                 self.insert_after(node.left, val)
#             else:
#                 self.insert_before(node.left, val)