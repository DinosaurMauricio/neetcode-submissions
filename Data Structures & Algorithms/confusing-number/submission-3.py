class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        result = 0
        temp = n
        while temp > 0:

            num = temp%10

            if num in [2, 3, 4,5,7 ]:
                return False

            if num == 6:
                num = 9
            elif num == 9:
                num = 6

            result = (result * 10 ) + num
            temp //= 10


    
        return not result == n