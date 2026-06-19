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
