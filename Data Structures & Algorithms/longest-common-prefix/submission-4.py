class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = []
        for i, s in enumerate(strs[0]):

            for string in strs:
                if s != string[i:i+1]:
                    return "".join(res)
                    
            res.append(s)

        return "".join(res)