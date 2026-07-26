class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix[0])

        for list_m in matrix:
            l,r = 0, n - 1

            while l <= r:
                mid = l + (r - l)//2
                if list_m[mid] >  target:
                    r = mid - 1
                elif list_m[mid] < target:
                    l = mid + 1
                else: # it found the target
                    return True

        return False