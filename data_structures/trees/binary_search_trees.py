class Node:
    def __init__(self, value: int):
        """Initialize a BST node with a value and null children."""
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None

    def delete_tree(self) -> None:
        """
        Delete the entire BST, freeing all nodes.
        Example:
            Input: tree = [5, 3, 7] -> Output: tree = empty
        Edge Cases:
            - Empty tree (no-op).
        """

        self.root = self.delete_using_post_traversal(self.root)
        
    def delete_using_post_traversal(self, node: Node):
        if node is None:
            return None

        node.left = self.delete_using_post_traversal(node.left)
        node.right = self.delete_using_post_traversal(node.right)
        
        return None

    def delete_value(self, value: int) -> None:
        """
        Delete the node with the given value from the BST, maintaining BST properties.
        If the value does not exist, do nothing.
        Example:
            Input: value = 3, tree = [5, 3, 7] -> Tree: [5, 7]
        Edge Cases:
            - Empty tree.
            - Deleting root, leaf, or node with one/two children.
            - Value not in tree.
        """
        if self.root is None:
            raise ValueError("Tree is empty")
        
        self._delete_node(self.root, value)
            
        
    def _delete_node(self, node: Node, value: int):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)
        elif value == node.value:
            if node.left is None and node.right is None:
                return None
            elif node.left is not None and node.right is None:
                return node.left
            elif node.right is not None and node.left is None:
                return node.right
            else:
                successor_node = self.get_successor_node(node)
                temp_value = successor_node.value
                self._delete_node(node, successor_node.value)
                node.value = temp_value
                return node
        return node


    def find_the_value_return_node(self, node: Node, value: int) -> Node:
        if node is None:
            return None
        
        if node.value == value:
            return node
        elif value < node.value:
            return self.find_the_value_return_node(node.left, value)
        else:
            return self.find_the_value_return_node(node.right, value)

    def get_successor(self, value: int) -> int:
        """
            Return the next-highest value in the BST after the given value, or -1 if none.
            Example:
                Input: value = 3, tree = [5, 3, 7] -> Output: 5
                Input: value = 7, tree = [5, 3, 7] -> Output: -1
            Edge Cases:
                - Empty tree.
                - Value not in tree (still find next-highest).
                - No successor (return -1).
        """

        if self.root is None:
            return -1
        
        current_node = self.root
        successor = None
        
        while current_node:
            if value < current_node.value:
                successor = current_node
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                if current_node.right:
                    successor = self.subtree_first(current_node.right)
                break
            
        return successor.value if successor is not None else -1

    def get_height(self) -> int:
        """
        Return the height of the BST (number of nodes along the longest path from
        root to leaf). A single node's height is 1; empty tree height is 0.
        Example:
            Input: tree = [5, 3, 7] -> Output: 2
            Input: tree = empty -> Output: 0
        Edge Cases:
            - Empty tree.
            - Single node.
            - Unbalanced tree.
        """
        if self.root is None:
            return 0
        
        return self._node_height(self.root)
    
    def _node_height(self, node: Node):
        if node is None:
            return 0
        
        return (1 + max(self._node_height(node.left), self._node_height(node.right)))
    
    def get_max(self) -> int:
        """
        Return the maximum value in the BST.
        Example:
            Input: tree = [5, 3, 7] -> Output: 7
        Edge Cases:
            - Empty tree (raise ValueError).
        """
        if self.root is None:
            raise ValueError("Tree is empty")
        
        max_node = self.subtree_last(self.root)

        return max_node.value
    
    def get_min(self) -> int:
        """
        Return the minimum value in the BST.
        Example:
            Input: tree = [5, 3, 7] -> Output: 3
        Edge Cases:
            - Empty tree (raise ValueError).
        """

        if self.root is None:
            raise ValueError("Tree is empty")

        min_node = self.subtree_first(self.root)
        
        return min_node.value

    def get_node_count(self) -> int:
        """
        Return the number of nodes in the BST.
        Example:
            Input: tree = [5, 3, 7] -> Output: 3
            Input: tree = empty -> Output: 0
        Edge Cases:
            - Empty tree.
            - Single node.
        """
        return self._node_count(self.root)

    def _node_count(self, node: Node) -> int:
        if node is None:
            return 0
        
        return (1 + self._node_count(node.left) + self._node_count(node.right))
    
    def get_successor_node(self, node: Node) -> Node:
        if node.right:
            return self.subtree_first(node.right)
        else:
            current_node = self.root
            while current_node.value != node.value:
                if node.value <= current_node:
                    successor = current_node
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            return successor
                 

    def insert(self, value: int) -> None:
        """
        Insert a value into the BST. If the value already exists, ignore it.
        Example:
            Input: value = 5, tree = empty -> Tree: [5]
            Input: value = 3, tree = [5] -> Tree: [5, 3]
        Edge Cases:
            - Empty tree (insert as root).
            - Duplicate values (ignore).
            - Unbalanced tree (insert maintains BST property).
        """
        if self.is_in_tree(value):
            return

        if self.root is None:
            self.root = Node(value)
            return

        self._insert_recursive(self.root, value)
        
    def _insert_recursive(self, node: Node, value: int) -> Node:
        if node is None:
            return Node(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return node
        
            
    def is_binary_search_tree(self) -> bool:
        """
        Return True if the tree is a valid BST, False otherwise.
        A valid BST has all left subtree values < node value < right subtree values.
        Example:
            Input: tree = [5, 3, 7] -> Output: True
            Input: tree = [5, 6, 7] -> Output: False
        Edge Cases:
            - Empty tree (valid).
            - Single node (valid).
        """

        return self._is_bst(self.root, float("-inf"), float("+inf"))
        
    def _is_bst(self, node: Node, min, max):
        if node is None:
            return True
        if node.value <= min or node.value >= max:
            return False
        return self._is_bst(node.left, min, node.value) and self._is_bst(node.right, node.value, max)
    
    def is_in_tree(self, value: int) -> bool:
        """
        Return True if the given value exists in the BST, False otherwise.
        Example:
            Input: value = 3, tree = [5, 3, 7] -> Output: True
            Input: value = 4, tree = [5, 3, 7] -> Output: False
        Edge Cases:
            - Empty tree.
            - Value at root or leaf.
        """
        if self.root is None:
            return False
        else:
            return self._find_target_value_in_subtree(self.root, value)

    def _find_target_value_in_subtree(self, node: Node, value: int) -> bool:
        if node is None:
            return False

        if value == node.value:
            return True
        elif value < node.value:
           return self._find_target_value_in_subtree(node.left, value)
        else:
           return self._find_target_value_in_subtree(node.right, value)
        
    def is_it_leaf_node(self, node: Node) -> bool:
        if node.left is None and node.right is None:
            return True
        else:
            return False
        
    def print_values(self) -> None:
        """
        Print all values in the BST in ascending order (in-order traversal).
        Example:
            Input: tree = [5, 3, 7] -> Output: 3 5 7
            Input: tree = empty -> Output: (nothing)
        Edge Cases:
            - Empty tree.
            - Single node.
        """
        self._helper_in_order_traversal(self.root)

    def _helper_in_order_traversal(self, node: Node):
        if node is None:
            return
        
        self._helper_in_order_traversal(node.left)
        print(node.value)
        self._helper_in_order_traversal(node.right)
    
    def subtree_first(self, node: Node):
        if node.left is None:
            return node
        
        return self.subtree_first(node.left)

    def subtree_last(self, node: Node):
        if node.right:
            return self.subtree_last(node.right)
        else:
            return node
