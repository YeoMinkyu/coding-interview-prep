# Booking.com Mock Interview: QuickSort & Sorting Algorithms

## Interviewee: Minkyu Yeo  
## Date: [June, 01, 2025]

---

### **Question 1: Why did you choose a random pivot when implementing partitioning in QuickSort?**

**My Answer:**  
Choosing a random pivot reduces the chance of always picking the smallest or largest value—especially if the input is already sorted or nearly sorted. Using a fixed pivot (first or last element) in these cases would cause unbalanced partitions and worst-case O(n^2) performance. Randomization helps ensure balanced partitions on average, keeping QuickSort’s time complexity at O(n log n).

**Feedback:**

- Choosing a fixed pivot(like `low` or `high`) leads to unbalanced partitions if the data is already sorted.
- That causes recursive calls of size `n-1`, `n-2`, ..., leading to **O(n²)** time.
- Randomizing the pivot helps ensure we avoid consistently bad splits, so on average, the recursion tree stays balanced and keeps QuickSort at O(nlogn).

---

### **Question 2: Why is your QuickSort in-place, and why isn’t it stable?**

**My Answer:**  
My implementation is in-place because all swaps and partitions are performed directly on the input array without extra memory allocation (except a few variables).  
QuickSort is not stable by default because swaps during partitioning may change the relative order of equal elements. While it’s possible to make QuickSort stable, it requires extra space and complexity, so for stable sorting I would use MergeSort.

**Feedback:**

- In-place: QuickSort rearranges elements within the input array, without allocating extra memory for another array - just a few variables for indices and the pivot
- In contrast, MergeSort mostly requires **O(n)** extra memory to merge arrays.
- Unstable : During swaps for partitioning, equal elements may cross over each other, so their original order can't be guaranteed.
- Making QuickSort stable is possible(by tracking original indices or extra keys), but it comes at the cost of extra memory and complexity, defeating the purpose of QuickSort's in-place nature.
- My conclusion, to choose MergeSort for stable sorting needs.

---

### **Question 3: If the input is already sorted in ascending order, will your QuickSort implementation still be efficient?**

**My Answer:**  
With random pivot selection, my implementation is more likely to remain efficient, because the chance of always picking the smallest or largest value is reduced. To further improve, I could use a “median-of-three” pivot strategy (choosing the median of three random elements), which further decreases the likelihood of unbalanced splits for sorted inputs.

**Feedback:**

- Random pivot selection already reduces the likelihood of picking the smallest or largest value, making unbalanced partitions much less likely and generally keeping performance at O(nlogn) even for sotrted arrays.
- Using the "median-of-three" strategy further increases the chance that the pivot splits the array in to roughly equal halves, even if the input is sorted or nearly sorted.
- This strategy is widely used in optimized versions of quicksort in practice(for example, C++ STL `std:sort()` uses a variant of this)

---

### **Question 4: Would you use QuickSort for sorting a linked list? Why or why not?**

**My Answer:**  
QuickSort is not well suited for linked lists because it relies on fast index-based access and swapping, which are inefficient in linked lists. MergeSort is a better choice for linked lists since it splits and merges nodes using only pointers—no index lookups needed. MergeSort is also stable and works in O(n log n) time for linked lists.

**Feedback:**

- QuickSort's efficiency depends on direct access to indexes, allowing for fast swaps and partitioning-which is natural for arrays, but not for linked lists.
- Linked lists don't provide O(1) access to arbitrary elements(because of no indexes!), so partitioning and swapping are slow and awkward, making QuickSort impractical for this data structure.
- MergeSort, in contrast, works beautifully on linked lists: you can split lists using the slow/fast pointer approach and merge them by relinking nodes, all in O(1) extra space per operation.
- Merge Sort is naturally suited for pointer-based data structures like linked lists because splitting and merging don’t require index-based access or element swapping.

---

## **Interviewer’s Feedback & Additional Professional Notes**

- Strong algorithmic understanding and clear real-world reasoning.
- Excellent awareness of time/space trade-offs and stability considerations.
- Good use of practical strategies (random pivot, median-of-three).
- Areas to deepen: Keep asking “Why not this algorithm here?” and practice ELI5 explanations.

---

## **Reflection**

- [ ] What did I do well in this mock interview?
- [ ] Where did I hesitate or get stuck?
- [ ] What sorting or partitioning topics should I practice next?

---

## **Next Steps**

- Practice coding both Lomuto and Hoare partitioning
- Review stable vs unstable sorts
- Add more “why not” notes for each algorithm
- Keep updating this Markdown log after each mock interview!

---
