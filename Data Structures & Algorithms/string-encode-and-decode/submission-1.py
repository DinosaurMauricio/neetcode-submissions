class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= rf"#{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        
        i = 0
        words = []
        while i < len(s):
            if s[i] == "#":
                j = i + 1
                while j < len(s) and s[j] != "#":
                    j+=1
                num = int(s[i+1:j])
                words.append(s[j + 1: j+num + 1])
                
                i = j + num + 1
            else:
                i+=1

        return words
