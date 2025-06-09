# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key == root.val:
            if not root.left and not root.right:
                return None
            elif not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                successor = self._get_successor(root.right)
                root.val, successor.val = successor.val, root.val
                root.right = self.deleteNode(root.right, successor.val)
            return root
        
        return root
    
    def _get_successor(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left:
            return self._get_successor(root.left)
        else:
            return root

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is not None and root.right is None:
                return root.left
            elif root.right is not None and root.left is None:
                return root.right

            else:
                successor = self.find_successor(root)
                temp_val = successor.val
                self.deleteNode(root, successor.val)
                root.val = temp_val
                return root

        return root

    def find_successor(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node.right:
            return self.find_subtree_first(node.right)

    def find_subtree_first(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node.left is None:
            return node

        return self.find_subtree_first(node.left)