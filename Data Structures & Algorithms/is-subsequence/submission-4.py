class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_p, t_p = 0, 0


        while t_p < len(t) and s_p < len(s):

            if t[t_p] == s[s_p]:
                s_p+=1

            t_p+=1

        return s_p == len(s)