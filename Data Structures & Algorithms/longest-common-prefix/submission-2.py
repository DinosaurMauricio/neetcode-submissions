class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = strs[0]
        max_l = 0

        for w in range(1, len(strs)):

            len_is = len(res) if len(strs[w]) > len(res) else len(strs[w])
            max_l=0
            for i in range(len_is):

                if strs[w][i] == res[i]:
                    max_l+=1
                else:
                    max_l = i
                    break

            res = res[:max_l]




        return res
