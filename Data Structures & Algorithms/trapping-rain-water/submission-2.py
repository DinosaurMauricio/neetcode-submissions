class Solution:
    def trap(self, height: List[int]) -> int:
        

        L, R = 0, len(height) - 1

        maxLeft, maxRight = height[L], height[R]
        total_water = 0 

        while L < R:
            #print(f"total water {total_water}, L {L} R {R}")
            if maxRight > maxLeft:
                L+=1
                maxLeft = max(height[L],maxLeft)
                total_water += maxLeft - height[L]
                
                
                
            else:
                R-=1
                maxRight = max(height[R],maxRight)
                total_water += maxRight - height[R]
                
            
        return total_water
        