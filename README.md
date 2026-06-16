## Notes

- **Length Prefixes** (Length + # + String)
Instead of putting all lengths at the beginning (like 1,2,3#a,aa,aaa), putting the length directly before each word (1#a2#aa) is way faster and cleaner, this is because we read characters until we hit #. Whatever is before # is always the length of the string. For example, if the length is 5, the decoder immediately grabs the next 5 characters as the word and moves on.
