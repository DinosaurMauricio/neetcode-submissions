class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")

        return "".join(res)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""

        i = 0
        res = []
        num = []
        #print(s)
        while i < len(s):
            #print(i)
            #print(res)
            if s[i] != '#':
                #while s[i].isdigit():
                num.append(s[i])
                i+=1
            else:
                number = int("".join(num))
                
                res.append(s[i + 1 : i + number+1])
                i += number + 1
                #print(len(num), number)
                num = []

        return res
