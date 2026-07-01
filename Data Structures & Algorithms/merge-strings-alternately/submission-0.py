class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = [None]*(len(word1) + len(word2))
        i, j , k = 0, 0, 0

        while j < len(word1) and k < len(word2):
            res[i] = word1[j]
            res[i+1] = word2[k]
            i+=2
            j+=1
            k+=1

        while j < len(word1):
            res[i] = word1[j]
            i+=1
            j+=1
        
        while k < len(word2):
            res[i] = word2[k]
            i+=1
            k+=1
        
        return "".join(res)

