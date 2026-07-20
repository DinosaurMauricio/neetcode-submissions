class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0

        unique_char = set("".join(s))

        for u in unique_char:
            l = 0
            temp = k
            for r in range(len(s)):
                if  s[r] != u:
                    if temp != 0:
                        temp-=1
                    else:
                        while s[l] == u:
                            l +=1
                        l+=1

                res = max(res, r - l + 1)
                #print(res)
            #print("other")

        return res
