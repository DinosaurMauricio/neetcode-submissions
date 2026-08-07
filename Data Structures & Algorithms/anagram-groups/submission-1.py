from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}


        for s in strs:
            vocab = [0]*26
            for char in s:
                vocab[ord(char) - ord('a')] += 1

            
            v_tuple =tuple(vocab)

            res.setdefault(v_tuple,[]).append(s)

        return list(res.values())
