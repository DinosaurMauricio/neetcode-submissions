class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_value = prices[0]
        res = 0
        for j in range(len(prices)):
            if prices[j] < min_value:
                min_value = prices[j]
            else:
                res= max(res, prices[j] - min_value)

        return res
        #other sol

        i, j = 0,0

        res = 0

        while j < len(prices) and i <=j:
            if j == i:
                j+=1
            elif prices[i] < prices[j]:
                res = max(res, prices[j] - prices[i])
                j+=1
                
            else:
                i = j 
        
        return res