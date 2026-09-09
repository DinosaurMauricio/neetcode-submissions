class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        #ops = {'+' : lambda x, y : x+y, 'C': lambda x: x.pop(), 'D': lambda x: 2*x }

        res = []
        for op in operations:
            if op == '+':
                res.append(res[-1]+ res[-2])
            elif 'C' == op:
                res.pop()
            elif 'D' == op:
                res.append(res[-1]*2)
            else:
                res.append(int(op))

        return sum(res)
