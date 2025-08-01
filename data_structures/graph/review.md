
## **1. Summary of Key Concepts**

### **Graph Representations**

* **Objects & Pointers:**
  Each node is an object with references (pointers) to its neighbors. Natural for OOP, but can be verbose in code and less cache-efficient.
* **Adjacency Matrix:**
  A 2D array where `matrix[u][v] = 1` (or the edge weight) if there is an edge from `u` to `v`.

  * **Pros:** Easy edge lookup (`O(1)`), good for dense graphs.
  * **Cons:** High space (`O(V^2)`), slow for iterating neighbors.
* **Adjacency List:**
  For each node, store a list (or set) of neighbors.

  * **Pros:** Space-efficient (`O(V + E)`), fast to iterate neighbors.
  * **Cons:** Edge lookup is `O(degree(u))`, not `O(1)`.
* **Adjacency Map (Dict):**
  Like an adjacency list, but with a dictionary (often for weights):
  `graph[u][v] = weight`.

  * **Pros:** Quick neighbor/weight lookup, great for sparse or weighted graphs.

### **BFS vs DFS**

* **BFS (Breadth-First Search):**
  Explores level by level from the start node (uses a queue).

  * **Time/Space Complexity:** `O(V + E)`
  * **Good For:** Shortest path in unweighted graphs, finding connected components.
* **DFS (Depth-First Search):**
  Explores as deep as possible before backtracking (uses stack or recursion).

  * **Time/Space Complexity:** `O(V + E)`
  * **Good For:** Detecting cycles, topological sort, connected components, SCCs.

---

## **2. Quiz/Interview Questions**

1. **When would you prefer an adjacency matrix over an adjacency list?**
- In an adjacency matrix, when the graph is dense, the memory space to represent an adjacency matrix is O(V^2), is not much worse than listing every edge, since the list would also be very large.
- In this case, if I often check whether an edge exists between two nodes, the constant time lookup of matrix is a big win.

**Strong answer**
- “I’d use an adjacency matrix when the graph is dense, meaning it has a large fraction of all possible edges. The adjacency matrix allows me to check for the existence (or weight) of an edge between any two nodes in constant time, O(1), by direct array indexing. This is much faster than the O(degree(u)) lookup needed in an adjacency list.
Since the matrix always uses O(V^2) space, it’s only efficient when there are enough edges to justify that cost. For sparse graphs, the space overhead is too large, and adjacency lists are preferable.
As an example, in algorithms where I need to check all pairs of nodes for connectivity, or when edge lookups are very frequent, adjacency matrices are a good fit—especially for dense graphs.”

2. **What’s the time and space complexity of BFS and DFS, and why?**
3. **How would you modify DFS or BFS to find all connected components in an undirected graph?**

---

## **3. LeetCode Problems for Practice**

* **Number of Provinces ([LeetCode 547](https://leetcode.com/problems/number-of-provinces/)):**
  Great for practicing adjacency matrix and finding components via BFS/DFS.
* **Course Schedule ([LeetCode 207](https://leetcode.com/problems/course-schedule/)):**
  Practice adjacency list and DFS (cycle detection/topological sort).

---

## **4. Common Mistakes or Misconceptions**

* **Misunderstanding time/space:**
  Forgetting that adjacency matrix is `O(V^2)` even for sparse graphs.
* **Queue vs Stack:**
  Accidentally using a stack in BFS or a queue in DFS!
* **Visited/Marking:**
  Not marking nodes as visited at the right time (leading to infinite loops).
* **One-off errors:**
  Off-by-one or index errors when translating from math to code.
* **Confusing neighbor access:**
  Misunderstanding which data structure makes it `O(1)` to check an edge.

---

## **5. (Optional) Challenge/Real-World Application**

> **Design a system for a ride-sharing company (like Uber) to model and update the city’s street map. Which graph representation would you choose, and why? How would you efficiently update the graph if a road closes or opens?**

---