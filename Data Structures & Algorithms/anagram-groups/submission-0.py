class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for i in range(len(strs)):
            vocab = [0]*26
            for v in strs[i]:
                vocab[ord(v) - ord('a')]+=1

            vocab = tuple(vocab)
                        
            res.setdefault(vocab,[]).append(strs[i])    

        return [r for r in res.values()]