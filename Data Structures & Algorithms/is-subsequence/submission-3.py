class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False

        if not s:
            return True

        s_p, t_p = 0, 0


        while t_p < len(t):

            #print(s_p)
            if t[t_p] == s[s_p]:
                s_p+=1

            if s_p == len(s):
                return True

            t_p+=1

        return s_p == len(s)