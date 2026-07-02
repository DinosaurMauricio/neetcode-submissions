class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operations ={
            "+": lambda a, b: a+b,
            "-": lambda a,b: b-a,
            "*": lambda a,b: a*b,
            "/": lambda a,b: int(b/a)
        }

        stack = []
        i = 0

        while i < len(tokens):
            print(stack)
            if tokens[i] in operations.keys():
                value1 = stack.pop()
                value2 = stack.pop()

                #print(value1,value2,value1/value2, value2/value1)

                res = operations[tokens[i]](value1,value2)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))

            i+=1

        return stack.pop()
