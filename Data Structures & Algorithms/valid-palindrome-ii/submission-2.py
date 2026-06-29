class Solution:
    def validPalindrome(self, s: str) -> bool:

        def validate(left, right) -> bool:
            while right < left:
                if s[left] != s[right]:
                    return False
                right+=1
                left-=1
            return True

        left = len(s) - 1
        right = 0
        remove_letter = False

        while right < left :
            

            if s[left] != s[right]:
                # call validPalindrome,
                # check first if the string by removing the 1 character to the left is correct if false
                # check the right is correct, if false return false as end, else return True
                return validate(left - 1, right) or validate(left, right + 1)

            left-=1
            right+=1
        else:
            return True