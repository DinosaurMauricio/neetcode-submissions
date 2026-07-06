class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        cars = zip(position, speed)
        cars_desc = sorted(cars, key = lambda x: x[0], reverse=True)

        stack = []

        for pos, spd in cars_desc:
            time = (target- pos) / spd
            if stack and  time <= stack[-1]:
                continue
            
            stack.append(time)
        return len(stack)
