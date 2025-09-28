# Two-Pointer Technique — Simple, Clear Explanation

## What is the two-pointer technique?

The **two-pointer technique** is a way to compare or process elements in a linear data structure (usually an array or a list) using two indices — called *pointers*. Instead of using a nested loop (which is usually O(n²)), two pointers let you solve many problems in **linear time O(n)** and **constant extra space O(1)** in typical cases.

The idea is to move the pointers according to simple, predictable rules until a condition is met.

---

## Why not just use nested loops?

A nested loop checks all pairs (or combinations) of elements. That works, but it costs a lot of time: **O(n²)**. Many problems have extra structure (for example: the array is sorted). When the input has such structure, we can predict how the pointers should move and avoid checking every pair.

This is where the two-pointer technique helps: it uses *predictable dynamics* to reduce the work.

---

## Predictable dynamics (easy idea)

**Predictable dynamics** means you know how elements relate to each other without checking every pair. For example, in a **sorted array**, every value to the right is greater than or equal to those on the left. That lets us make safe decisions:

* If we want a larger sum, we move the pointer to the right.
* If we want a smaller sum, we move the pointer to the left.

Because the structure is predictable, we can move pointers in ways that are guaranteed to make progress.

---

## The three main two-pointer approaches

There are three common patterns. I explain each, tell when to use it, show short pseudocode, and give a simple example.

### 1) Inward traversal (two ends — move inward)

**When to use:**

* The array is sorted (or you can reason about relative order easily).
* You need a pair of indices (for example, two-sum in sorted array, pair that sums to target).

**Idea:**

* Put one pointer at the start (`left`) and one at the end (`right`).
* Move them toward each other based on conditions until they meet or cross.

**Pseudocode (find two numbers that sum to `target`):**

```python
left = 0
right = n - 1
while left < right:
    s = arr[left] + arr[right]
    if s == target:
        return (left, right)
    elif s < target:
        left += 1
    else:
        right -= 1
return None
```

**Complexity:** Time O(n), Space O(1).

**Detailed example (step-by-step):**

* Array: `[1, 2, 3, 4, 5]`, target = 6
* Start: left=0 (1), right=4 (5) → sum = 6 → found `(0,4)`.

If sum wasn't equal, you would move the pointer that helps get closer to the target.

**Note about `left < right` vs `left <= right`:**

* Use `left < right` when the problem requires two **different** indices.
* Use `left <= right` only when a single element can be used twice or the problem explicitly allows the same index twice (rare for pair problems).

---

### 2) Unidirectional traversal (same direction / sliding window)

**When to use:**

* You want to find a subarray or window that satisfies some property (sum, length, average, count, etc.).
* Often the array elements are non-negative (so expanding the window always increases the sum). If negatives exist, sliding-window needs extra care.

**Idea:**

* Use two pointers `left` and `right` that both move from left to right.
* `right` expands the window to gather information. `left` shrinks the window when conditions are not satisfied.

**Pseudocode (find shortest subarray with sum >= target, assuming non-negative numbers):**

```python
left = 0
current_sum = 0
best_len = infinity
for right in range(n):
    current_sum += arr[right]
    while current_sum >= target:
        best_len = min(best_len, right - left + 1)
        current_sum -= arr[left]
        left += 1
# best_len holds answer or infinity if not found
```

**Complexity:** Time O(n) — each element enters and leaves the window at most once. Space O(1).

**Intuition:** `right` finds candidate windows; `left` removes elements until the candidate fails the condition.

---

### 3) Staged traversal (outer pointer + inner pointer)

**When to use:**

* You need to gather extra information for each element or for each position — for example, count pairs with difference ≤ k, or find the farthest `j` that works for each `i`.
* The inner pointer never moves back to the left; both usually move forward.

**Idea:**

* For each `i`, advance `j` (a second pointer) as far as needed. Because `j` only moves forward overall, the total work is linear.

**Pseudocode (count pairs with `arr[j] - arr[i] <= k`, sorted array):**

```python
count = 0
j = 0
for i in range(n):
    while j < n and arr[j] - arr[i] <= k:
        j += 1
    # now arr[j] - arr[i] > k or j == n
    # pairs with i are indices (i+1) .. (j-1)
    count += (j - 1) - i
```

**Complexity:** Time O(n). Space O(1).

**Note:** This is like a two-pointer version of a sliding window but framed as "for each i, find the farthest j".

---

## When to choose the two-pointer approach

Use two pointers when:

* The input is a **linear** structure (array, list, string).
* There is a **predictable order** (sorted array or monotonic condition) or you can reason about how moving pointers changes the outcome.
* The problem asks about pairs, subarrays, or something that can be built by combining two indices.

**Common problem patterns that hint at two-pointers:**

* "Find a pair that adds to X." (two-sum on sorted array)
* "Find the longest/shortest subarray with property P." (sliding window)
* "Count pairs/triples with constraints on differences or sums." (staged traversal)

---

## Real-world use case: memory compaction (garbage collector)

A common real-world example is **memory compaction** in a garbage collector. Two pointers are used: `free` and `scan`.

* `free` points to the next free spot where we should move a live object.
* `scan` walks the heap scanning objects.

When `scan` finds a live object, the object is moved to the `free` location and `free` advances. `scan` continues scanning after the object. Over time, this moves all live objects toward one end of memory and frees up a continuous block of space.

This is exactly like a two-pointer partitioning: one pointer marks where to place items (`free`), the other finds items to keep (`scan`). It's efficient and in-place.

---

## Important details, tips, and common mistakes

* **Always reason about pointer movement:** Make sure every pointer change moves you closer to the end condition. That avoids infinite loops.
* **Boundaries matter:** Use `left < right` when you want two different indices. Use `left <= right` only when allowed to use the same element twice.
* **When elements can be negative:** Sliding-window (unidirectional) might not work if adding an element can make the window "better" or "worse" unpredictably. For arrays with negatives, staged traversal or other techniques may be safer.
* **Avoid re-scanning backwards:** Many two-pointer approaches rely on the fact that the second pointer never goes back. If you move pointers back and forth often, you may lose linear time.
* **Handle duplicates carefully:** If the problem asks for unique pairs or unique triplets, you must skip duplicates explicitly.
* **Check initial positions:** Some problems start pointers at `0`, others at `1` or at the ends. Match initial positions to the problem.

---

## Complexity summary

* Typical two-pointer solutions run in **O(n)** time.
* Extra space is usually **O(1)** (not counting the input). If you need extra bookkeeping (like storing results), space can grow.

---

## Quick checklist to decide if two-pointers will help

1. Is the input linear (array/string)?
2. Is the array sorted or can you reason about order? Or does the problem ask about contiguous subarrays?
3. Is the problem about pairs, windows, or relationships between two indices?

If most answers are yes, try a two-pointer approach.

---

## Short practice problems (to try)

* Two-sum in a **sorted** array (find indices for a target sum).
* Remove duplicates from a sorted array in-place (write the array without duplicates).
* Find the longest subarray with sum equal to `k` (if elements non-negative).
* Count pairs with difference ≤ `k` in a sorted array.

---

## Closing notes

Two-pointers is a small set of ideas that covers many problems. The key is to spot *predictable dynamics* and then design simple pointer-move rules that always make progress. Keep practicing — after a few


