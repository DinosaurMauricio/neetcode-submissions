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
