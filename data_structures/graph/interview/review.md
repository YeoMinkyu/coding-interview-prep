
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

### 1. **When would you prefer an adjacency matrix over an adjacency list?**
- In an adjacency matrix, when the graph is dense, the memory space to represent an adjacency matrix is O(V^2), is not much worse than listing every edge, since the list would also be very large.
- In this case, if I often check whether an edge exists between two nodes, the constant time lookup of matrix is a big win.

**Strong answer**
- “I’d use an adjacency matrix **when the graph is dense**, meaning it has a large fraction of all possible edges. The adjacency matrix allows me to check for the existence (or weight) of an edge between any two nodes in **constant time, O(1)**, by **direct array indexing**. This is much faster than the O(degree(u)) lookup needed in an adjacency list.
Since the matrix always uses O(V^2) space, it’s only efficient when there are enough edges to justify that cost. For sparse graphs, the space overhead is too large, and adjacency lists are preferable.
As an example, in algorithms where I need to check all pairs of nodes for connectivity, or when edge lookups are very frequent, adjacency matrices are a good fit—especially for dense graphs.”

### 2. **What’s the time and space complexity of BFS and DFS, and why?**

**Strong answer:**

**Time Complexity: `O(|V| + |E|)`**

* Both **BFS** and **DFS** have time complexity `O(|V| + |E|)`, where `|V|` is the number of vertices (nodes) and `|E|` is the number of edges.
* **Why?**

  * Every node is visited at most once.
  * For each node, you look at each of its edges (either from its adjacency list, or by scanning its neighbors).
  * So, across the whole traversal, every edge is considered at most twice (once from each end in an undirected graph).
  * This leads to total work:

    * **BFS/DFS visit each node once:** `O(|V|)`
    * **Look at each edge once:** `O(|E|)`
    * Combined: `O(|V| + |E|)`

---

### **Space Complexity**

* **BFS:**

  * Uses a queue to keep track of nodes at the current “level.”
  * In the worst case (for example, a very wide tree), the queue might contain up to `O(|V|)` nodes.
  * Also needs a “visited” set or array (`O(|V|)`).
  * **Space:** `O(|V|)`
* **DFS:**

  * Uses a stack (explicit or via recursion). In the worst case (e.g., a long linear chain), the stack can grow up to `O(|V|)` deep.
  * Needs a “visited” set or array (`O(|V|)`).
  * **Space:** `O(|V|)`

---

### **Key Differences (for clarity)**

* **Traversal order:**

  * *BFS* explores nodes in layers (all nodes at distance 1, then 2, etc.), which is good for finding shortest paths in unweighted graphs.
  * *DFS* explores as deep as possible before backtracking, which is useful for tasks like cycle detection, topological sort, etc.
* **Space nuance:**

  * BFS can require lots of space if a level is very “wide” (many nodes at the same depth).
  * DFS uses stack space proportional to the *depth* of the search.

---


## **If You’re Asked in an Interview, You Can Say:**

> “Both BFS and DFS run in O(V + E) time, since they visit every node and explore every edge exactly once. Their space complexity is O(V) due to the need to keep track of visited nodes and, for BFS, the queue, or for DFS, the stack. The difference is in their traversal order—BFS explores nodes level by level, which can require more space for very wide graphs, while DFS explores as deep as possible, using space proportional to the depth of the graph.”

---

## 250816
### Quiz / Interview Questions

Q1:
Why does BFS guarantee the shortest path in an unweighted graph, but DFS does not?

Q2:
If we store (node, path) in BFS instead of (node, distance), what trade-offs are we making in terms of time and space complexity?

Q3:
How would you modify BFS to not only return the distance but also reconstruct the exact path from the source to the destination?

## 250816
### Quiz / Interview Questions

### Q1: Why does BFS guarantee the shortest path in an unweighted graph, but DFS does not?
- In an unweighted graph, BFS explores nodes level by level from the source. That means the first time we see a node, we’ve already used the fewest edges possible to get there. So BFS guarantees the shortest path.
On the other hand, DFS explores as deep as possible before backtracking. It might reach a node through a longer path before it ever explores the shorter path, so it cannot guarantee the shortest path.
That’s why BFS is preferred for shortest path problems in unweighted graphs, while DFS is better for exploring or detecting structures like cycles or connectivity.

### Q2: If we store (node, path) in BFS instead of (node, distance), what trade-offs are we making in terms of time and space complexity?

### Q3: How would you modify BFS to not only return the distance but also reconstruct the exact path from the source to the destination?

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