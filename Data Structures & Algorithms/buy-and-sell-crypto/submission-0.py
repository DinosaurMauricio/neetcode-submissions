class Solution:
    def maxProfit(self, prices: List[int]) -> int:

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