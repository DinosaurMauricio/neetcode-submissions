## Notes

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
