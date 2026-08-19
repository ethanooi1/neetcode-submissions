class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == '+':
                x = int(stack[-1])
                y = int(stack[-2])
                stack.append(str(x + y))
            elif operations[i] == 'D':
                stack.append(str(int(stack[-1]) * 2))
            elif operations[i] == 'C':
                stack.pop()
            else:
                stack.append(operations[i])
        
        sum = 0
        for n in range(len(stack)):
            sum += int(stack.pop())
        
        return sum
