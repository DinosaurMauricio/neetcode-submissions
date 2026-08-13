class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        previous = -1
        for i in range(len(arr) - 1 , - 1, -1):
            temp = arr[i]
            arr[i] = previous


            if temp > previous:
                previous = temp

        return arr
