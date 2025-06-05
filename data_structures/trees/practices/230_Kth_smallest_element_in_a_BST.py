# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None

        def in_order_traversal(root: Optional[TreeNode], k: int) -> None:    
            if root is None or self.result is not None:
                return

            in_order_traversal(root.left, k)
            self.count += 1
            if self.count == k:
                self.result = root.val
                return
            in_order_traversal(root.right, k)

        in_order_traversal(root, k)

        return self.result
        