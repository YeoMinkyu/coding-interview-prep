# Mock Interview: Binary Search Tree (BST)

**Interviewee:** Minkyu Yeo  
**Date:** [June, 06, 2025]

---

## **Question 1:**  

**Describe how you would insert a value into a Binary Search Tree (BST). What’s the time complexity for this operation?**

### My Answer

I will insert a given value into a binary search tree based on the node it already inserted in the tree. If a value is lesser than a node that I can compare with a given value that I want to insert into binary search, if the value is lesser than the current node's value, I want to insert the left child node. In contrast, if the given value is greater than the current value of the node, I will insert the right child. If it's the worst case of time complexity, it will be the height of this binary search tree. Maybe it will be O(log n) because the height is approximately log n. But if the binary search tree is kind of looks like linked list because all values are greater than root value and again, iteratively, the right child of root value is also greater than any less than any node, it will be kind of just linked list, kind of sorted linked list in ascending order, it will be time complexity is O of n. So, the worst case, it will be O of n.

### Feedback

- Correct logic for BST insertion.
- Accurately described both average and worst-case time complexities (O(log n) and O(n)).
- Great awareness of degenerate/linked-list cases.
- For even more clarity: Mention insertion is O(h) (height), and that self-balancing BSTs guarantee O(log n).

---

## **Question 2:**

**What is the time complexity for searching for a value in a perfectly balanced BST vs. a completely unbalanced BST? (Explain your reasoning.)**

### *My Answer*

The time complexity for searching a value is same with the time complexity for inserting a value in the tree. In case of perfectly balanced BST, the time complexity will be O of log n. In the worst case, it will be placed the lowest of height in the tree. So if we can get the height of the tree, we can estimate the time complexity for searching. It will be also all of log n. So the worst case, the time complexity will be also O of log n. But in the case of a completely unbalanced BST, it looks like same with the linked list. All nodes are connected behind the tail. The node indicates the next node. And iteratively, the next node also indicates the next node. So the time complexity for searching in a completely unbalanced BST, it will be the same the time complexity with linked list. So it should traverse all nodes, in the worst case, n nodes, for searching a value in the end of the list. So it will be O of n.

### Feedback

- Solid answer, recognizing search complexity is tied to tree height.
- Correct O(log n) for balanced, O(n) for unbalanced/linked-list shape.
- Clear reasoning for both scenarios.
- Tip: Explicitly mention “O(log n) only for balanced BSTs.”

---

## **Question 3:**

**How would you delete a node with two children in a Binary Search Tree? (Walk me through your logic and reasoning.)**

### My Answer

When I intend to delete a node with two children in a BST, before deleting the node, I will find the successor of the current node that I want to delete. The successor of the current node means the value of the successor will be always next greater value of the current node that I want to delete. And the successor has two possibilities that one is leaf node and one is the node with one child. As the algorithm of deleting a node in BST, in just case of leaf node, just we can't delete it, just we can't disconnect the node from the parent node. That's all. So it will be easy if I change the current value that I want to delete with the successor node. So always it will be, the one case it will be leaf node, after changing two nodes and I can't delete if the successor was leaf node. And another case, it will be the successor node is with the node with one child. So after changing the value between the two nodes, and after then iteratively I can find which side of this successor has child node. If the left node, whether if the right node or left node, just I can easily connect with the parent's node with the child node of the successor. So it is the way I can delete the node with two children in a BST.

### Feedback  

- Correct understanding of using the in-order successor for deletion.
- Good awareness of both leaf and single-child cases for the successor.
- Communicated that after replacement, deletion reduces to simpler cases.
- For conciseness, in interviews say: “Replace value with in-order successor, then delete successor node.”

---

## **Next Steps / Reflection**

- [ ] Consider practicing with code for each operation.
- [ ] Practice describing each operation aloud for interview speed/clarity.
- [ ] Try advanced BST problems (e.g., finding kth smallest, augmenting with subtree sizes).

---

## **Optional Advanced/Follow-Up Questions**

- How would you design a BST to find the kth smallest element in O(log n) time?
- How would you keep a BST always balanced?
- Can you implement an iterative in-order traversal?

---
