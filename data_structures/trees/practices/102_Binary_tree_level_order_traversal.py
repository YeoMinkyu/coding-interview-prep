"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Using BFS

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        output = []
        
        if not root:
            return output
        
        level = 0
        queue = deque([(root, level)]) # TreeNode object, level        
        level_nodes = defaultdict(list)
        level_nodes[level].append(root.val)

        while queue:
            node, level = queue.popleft()

            if node.left:
                queue.append((node.left, level+1))
                level_nodes[level+1].append(node.left.val)
               
            if node.right:
                queue.append((node.right, level+1))
                level_nodes[level+1].append(node.right.val)
             
        for _, nodes in level_nodes.items():
            output.append(nodes)

        return output