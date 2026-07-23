## Notes

# Array and Two Pointers

- **Length Prefixes** (Length + # + String)
Instead of putting all lengths at the beginning (like 1,2,3#a,aa,aaa), putting the length directly before each word (1#a2#aa) is way faster and cleaner, this is because we read characters until we hit #. Whatever is before # is always the length of the string. For example, if the length is 5, the decoder immediately grabs the next 5 characters as the word and moves on.


- **Anchor Identification / Hash Set Lookups**
When searching for the boundaries or lengths of continuous sequences in unsorted data we can use a Hash Set for $O(1)$ lookups and identify the number that is a starting point.

$Identify the Anchor$: Filter out redundant processing by checking if the element's predecessor (`num - 1`) exists. If it doesn't, you have found a guaranteed starting point.

$Local Expansion$: Once the anchor is verified, using a `while` loop to expand the sequence forward (`num + 1`). Because each element is only visited a constant number of times, the overall time complexity drops to $O(n)$.
  
Reminder: Don't think, "Oh, I have to traverse the algorithm but numbers are all over the place." While it's okay to reorder, it makes it $O(n \log n)$. Just think, "Well, I just have to check they are there like in a dict (`num in array`)!" As order doesn't really matter now

```python
# Check if it's a starting point, then use another while loop to check if they are there
num_set = set(nums)

if (num - 1) not in num_set:  # It's a starting point
    while (num + 1) in num_set:  # Just check they are there
        num += 1
```

- **Boundary Tracking / Hash Map Lookup**
We can keep track of the boundaries using hashmap. In the first step, we see if the current position already exists. In other words, we check if our neighbors already existed. If they do, it means I count myself and my neighbors that exist.

Then we update our outer boundaries—telling them, "Yeah, I'm your neighbor now, so extend the total sequence length." This is what is happening in the steps `mp[num - mp[num - 1]] = mp[num]` and `mp[num + mp[num + 1]] = mp[num]` to update the absolute left and right edges. After that, it just updates the max value.

```python
def longestConsecutive(self, nums: List[int]) -> int:
    mp = defaultdict(int)
    res = 0

    for num in nums:
        if not mp[num]:
            mp[num] = mp[num - 1] + mp[num + 1] + 1
            mp[num - mp[num - 1]] = mp[num]
            mp[num + mp[num + 1]] = mp[num]
            res = max(res, mp[num])
    return res
```

- **Two Pointers (Area)**
When a problem asks to maximize an area (like a rectangle), a great approach is putting pointers at the very start and end. This lets you start with the maximum possible width. From there, the trick is knowing which one to move: since the area is always limited by the shorter pillar, we keep the taller pillar still while the samller one move in its next direction till we find a smaller pillar.

```python
l, r = 0, len(height) - 1
    #.... logic here
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
```

- **Two Pointers (Sorted Arrays)**
When a problem specifies a "non-decreasing" (e.g. [1,2,3,4]) or sorted array we can place one pointer at the start (`left`) and one at the end (`right`), we can confidently shrink our search space based on the current sum relative to a target:
  * If `current_sum > target`: Move `right` inward to decrease the sum.
  * If `current_sum < target`: Move `left` outward to increase the sum.

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        cur_sum = nums[left] + nums[right]
        if cur_sum == target:
            return [left, right]
        elif cur_sum > target:
            right -= 1
        else:
            left += 1
```

- **Three pointers**
We can scale the previous two-pointer logic to find three numbers that sum to a target (like 0) by fixing one number as a pivot and using two pointers for the rest of the array.

Since the array is sorted, the biggest challange is to deal with duplicate numbers which cause duplicate results. We solve this by skipping identical values for both the pivot and the moving pointers.

e.g. in [1,0,0,4,5]
By the time the search reaches the double zero, the next iteration is going to find the same operation. To fix this, we can just check the previous element and ignore it if it exists to increase to the following element.


```python
# Skip duplicate pivots
if i > 0 and nums[i] == nums[i - 1]:
    continue

# Skip duplicate left pointers (inside the while loop)
while left < right and nums[left] == nums[left - 1]:
    left += 1
```

- **Binary Search & Overflow Prevention**
Binary search cuts the search space in half each cycle, achieving O(log n) time complexity. 

To calculate the midpoint without risking integer overflow (e.g., when adding two massive index values like `low + high`), use the subtraction offset method instead of the standard formula:
   
   $Standard (Risk of overflow):$ `(low + high) // 2`
   
   $Safe:$ `low + (high - low) // 2` (where `(high - low) // 2` is the distance, and `+ low` is the offset).

If `mid` is not the target, we shift the boundaries to `mid + 1` or `mid - 1` because the current `mid` has already been checked.

```python
def binarySearch(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1      # Target is higher
        else:
            high = mid - 1     # Target is lower
    return -1
```

- **Horizontal Scanning (Longest Common Prefix)**
Horizontal scanning checks a list of strings character-by-character (vertically) using the first word as a baseline. This avoids checking full words unnecessarily or worrying about their true sizes.

We iterate through the index i of the first word and compare it across all other strings s. We stop and return the sliced prefix s[:i] the exact moment a mismatch occurs or a word runs out of letters.

$The Stopper$ (i == len(s)): Handles shorter words. If index i hits the length of the current word, it means we ran out of letters to check. We stop here to prevent an IndexError.

$The Break$ (s[i] != strs[0][i]): Triggers the moment a character doesn't match the baseline word.

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return s[:i]
    return strs[0]
```

- **Boyer-Moore Voting Algorithm (Majority Element)** 
Used to find the element that appears more than $\lfloor n/2 \rfloor$ times. Assumption: A majority element must exist, otherwise the result may be incorrect (e.g., [3,3,1,1] fails).The algorithm uses a candidate and a count. We iterate through the array, treating the process like a vote:

If count == 0, we pick the current element as the new candidate.

If the current element matches the candidate, count += 1.

If it doesn't match, count -= 1 (the current element "cancels out" a vote for the candidate).

```python
def majorityElement(self, nums: List[int]) -> int:
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
```

- **Merge Sort**
A divide-and-conquer **sorting** algorithm that guarantees a constant time complexity of $O(n \log n)$. It breaks the problem down into two main phases using recursion:

 1. **Divide:** Split the array in half at the middle index repeatedly until every subarray contains only a single element.
 2. **Conquer (Merge):** Recombine and sort the subarrays using a **3-pointer method**. We compare elements from two halves, place the smaller one into the original array, and once one half is exhausted, copy over the remaining elements.

>Complexity Analysis
>* **Divide O(log n):** We split the array of size $n$ in half repeatedly. This means we divide $n$ by $2$ a total of $x$ times until the size is $1$:
>$$\frac{n}{2^x} = 1 \implies n = 2^x \implies x = \log_2 n$$
>* **Merge O(n):** At each level of recursion, we must traverse and recombine all elements in the array.
>* **Total Time Complexity:** Because the merge step depends on the division steps, the final time complexity is $O(n \log n)$.
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums

```

- **Bucket sort**
When elements fall within a known, finite range, we can count the occurrences of each value in a first pass. For in-place sorting, we rewrite the original array sequentially using these counts without doing any traditional swaps.

The main limitation is that you must know the exact range of values beforehand to allocate your counting buckets.

```python
# First pass: Count frequencies
counts = {0: 0, 1: 0, 2: 0}
for n in nums: 
    counts[n] += 1

# Second pass: Overwrite in-place
i = 0
for val in sorted(counts_map.keys()):
    for _ in range(counts[val]):
        nums[i] = val
        i += 1
```

e.g., in [2, 0, 1, 2]
Our counts are {0: 1, 1: 1, 2: 2}. We overwrite the array by filling one 0, one 1, and two 2s in order.

- **Dutch National Flag**
An expansion of the partitioning concept where we use boundaries to isolate elements. By using a left pointer l for 0s, a right pointer r for 2s, and a scanner i, we aggressively kick extremes to the edges, leaving 1s naturally trapped in the middle.

The biggest challenge is managing the scanner i: when swapping a 2 from the right, the incoming element is completely un-scanned, so we must freeze i in place for an iteration to inspect it.

e.g., in [1, 2, 0] with l=0, r=2, i=1 (pointing at 2)
We swap index i and r, changing the array to [1, 0, 2]. We shrink the r boundary, but keep i=1 so we can inspect the newly arrived 0 on the next loop

```python
while i <= r:
    if nums[i] == 0:
        nums[i], nums[l] = nums[l], nums[i]
        l += 1
        i += 1
    elif nums[i] == 2:
        nums[i], nums[r] = nums[r], nums[i]
        r -= 1 # Freeze i to inspect the incoming element
    else:
        i += 1
```

- **Sliding window**
Think of it like looking through a moving frame. If an array has 10 elements but our window size is 3, we can only see elements 0–2, then 1–3, then 2–4, etc. This is super useful for checking things within a specific range, like finding a duplicate nearby. We use two pointers to track the start and end of the window. We usually start at 0 and let the right side grow, shrinking the left side only when needed. A huge hint for this pattern is when a problem asks for something within a range of j - i <= k.

The core mechanic relies on two pointers ($L$ and $R$). As $R$ expands the window to explore new elements, $L$ gets smaller it from behind whenever a constraint is violated (like the window size exceeding $k$).

```python
window = set()
L = 0

for R in range(len(nums)):
    # Window grew past size k, slide the left side in
    if R - L > k:
        window.remove(nums[L])
        L += 1
    
    # Check if we found a duplicate in our current window
    if nums[R] in window:
        return True
    
    window.add(nums[R])
```

# Stack

- **MinStack (Two-Stack Approach)**
We can use a secondary stack (minStack) to mirror the main stack's history. Using only one variable would break when that minimum is popped (because the element is not anymore on the stack), for this reson we we log the minimum element at each time. 

By using both stacks, popping an element automatically reveals the previous minimum right at the top of the minStack.

e.g., in [2, 5, 1]:
* Push 2: stack = [2], minStack = [2]
* Push 5: stack = [2, 5], minStack = [2, 2] (since 2 < 5)
* Push 1: stack = [2, 5, 1], minStack = [2, 2, 1]
When we pop 1, the minStack also pops, instantly restoring 2 as the historical minimum.

```python
def push(self, val: int) -> None:
    self.stack.append(val)
    # Grab the current min from the top, or use val if empty
    val = min(val, self.minStack[-1] if self.minStack else val)
    self.minStack.append(val)

def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop() # Automatically restores the previous minimum
```

- **MinStack (Space Optimized Math / Tripwire Approach)**
To optimize the previous approach and instead use only one variable, we use the difference between the incoming value and the current minimum: `val - self.min`.

Its identical to the two-stack approach because we must keep track of history, but we use a negative value as a trigger. When we pop and see a negative, we think: "ok, this was a change that changed the min value", in case its a positve value there was no change the previous element was much bigger so it cannot be a min. To reconstruct the past, we "sum" (via double negatives) that stored difference back into our tracking variable to restore the exact minimum value that we beat before.


e.g., with self.min = 2 and pushing 1:
We push the difference 1 - 2 = -1 onto the stack and update self.min = 1. 
When popping -1, the negative sign triggers an alarm: we reconstruct the old minimum by doing 1 - (-1) = 2, restoring what we beat before.

```python
def push(self, val: int) -> None:
    if not self.stack:
        self.stack.append(0)
        self.min = val
    else:
        self.stack.append(val - self.min)
        if val < self.min:
            self.min = val

def pop(self) -> None:
    pop = self.stack.pop()
    if pop < 0:
        self.min = self.min - pop
```

- **Monotonic Stack & Sorting**
When dealing with disordered, moving elements (like cars on a road), sorting them by position in descending order simplifies the problem by letting us evaluate interactions from front to back. 

Instead of simulating the movement step-by-step with loops, we use a mathematical approach to calculate the time to destination upfront: `time = (target - position) / speed`. 

The core mechanic relies on a monotonic stack to track fleets. If a car behind takes less than or equal time (`time <= stack[-1]`) to reach the target than the car ahead of it, it will inevitably catch up and join that fleet, so we ignore it. If it takes longer, it becomes the leader of a new, slower fleet.

```python
# Sort cars by position in descending order (closest to target first)
cars_desc = sorted(zip(position, speed), reverse=True)
stack = []

for pos, spd in cars_desc:
    time = (target - pos) / spd
    # If the current car arrives sooner or at the same time as the fleet ahead,
    # it catches up and merges. We skip adding it to the stack.
    if stack and time <= stack[-1]:
        continue
    
    stack.append(time)
```

# Trees
- **Traversing trees**
To traverse trees the easiest way to do it is by using recursive methods.

```python
        def traverse(root):

            if not root:
                return 
            traverse(root.left)
            traverse(root.right)

        traverse(root)
```

But you can also iterate with it with the help of a stack for example. In here we would have to traverse the left node till it is None, after that we can simply pop the last element (the leaf of the left node), process it, and go set the right node.
```python
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop().right
```

Previous solution is good for pre and in order traverse but for post we take a different approach, we can use another stack for validation. And we can organize the stack such that the last elements are pushed first and the left nodes which go first are added last:

```python
        res = []
        stack, visited = [root], [False]

        while stack:
            node, v = stack.pop(), visited.pop()
            if node:
                if v:
                    res.append(node.val)
                else:
                    stack.append(node)
                    visited.append(True)
                    stack.append(node.right)
                    visited.append(False)
                    stack.append(node.left)
                    visited.append(False)
```

# Sliding Window

- **Character Replacement (Sliding Window)**
A dynamic window concept where we stretch right `r` to explore and shrink left `l` to keep things valid. We count the frequency of our most popular character (`maxf`), and the difference between total window size and `maxf` is the key. 

If there’s a huge difference, it means we have way more of one character than others. We then ask: "How many other characters do we have to swap?" If the count is above `k` we move `l` to the right to remove elements from the back until it's okay again.

e.g., in "AABABBA" with `k=1`, suppose our window is `[A, A, B, C]` (`l=0, r=3`).
Window size is 4, max char (`A`) is 2. The difference is `4 - 2 = 2` other characters. Since `2 > k`, we move `l += 1` to kick elements out from the back until the difference is back down to $\le 1$.

```python
for r in range(len(s)):
    count[s[r]] = 1 + count.get(s[r], 0)
    maxf = max(maxf, count[s[r]])

    # If non-major characters exceed k, shrink window from the left
    while (r - l + 1) - maxf > k:
        count[s[l]] -= 1
        l += 1
    res = max(res, r - l + 1)
```

# Binary Search
- **Binary Search: Lower & Upper Bounds**
An extension of binary search where instead of stopping at the first target match, two boundary pointers `l` and `r` squeeze together to trap the outer edges of a repeated target value or insertion point.

The biggest challenge is knowing *which* pointer pushes forward when `nums[m] == target`:
- **Lower Bound (`>= target`):** Finds the **first** occurrence. When `nums[m] == target`, `r` treats it as "far enough right" and shrinks left (`r = m`) to search for an earlier match. `l` only steps forward (`l = m + 1`) when `nums[m]` is strictly smaller than the target.
- **Upper Bound (`> target`):** Finds the **first element strictly greater** than the target. When `nums[m] == target`, `l` treats it as "too small" and steps right past it (`l = m + 1`). `r` shrinks left (`r = m`) only when `nums[m]` is strictly greater than the target.

e.g., in `[1, 3, 5, 5, 5, 8]` searching for target `5`:
For **Lower Bound**, hitting `nums[2] = 5` makes `r` pull left to index 2 to see if an earlier 5 exists. 
For **Upper Bound**, hitting `nums[2] = 5` makes `l` push past it to index 3 to find the first element *after* the 5s.

Both algorithms end when `l == r`, leaving `l` standing on the target boundary.

```python
# Lower Bound: First index where nums[i] >= target
def lower_bound(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = l + (r - l) // 2
        if nums[m] >= target:
            r = m      # Target found or exceeded; shrink right wall left
        else:
            l = m + 1  # Too small; step left wall past m
    return l

# Upper Bound: First index where nums[i] > target
def upper_bound(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = l + (r - l) // 2
        if nums[m] > target:
            r = m      # Strictly greater found; shrink right wall left
        else:
            l = m + 1  # Target or smaller; step left wall past m
    return l
```
