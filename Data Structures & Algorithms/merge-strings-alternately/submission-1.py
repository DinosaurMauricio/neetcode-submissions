class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = [None]*(len(word1) + len(word2))

        wp = 0
        wp2 = 0
        i = 0

        while wp < len(word1) and wp2 < len(word2):
            res[i] = word1[wp]
            res[i + 1] = word2[wp2]
            wp+=1
            wp2+=1
            i+=2
        
        while wp < len(word1):
            res[i] = word1[wp]
            i+=1
            wp+=1

        while wp2 < len(word2):
            res[i] = word2[wp2]
            i+=1
            wp2+=1

        return "".join(res)