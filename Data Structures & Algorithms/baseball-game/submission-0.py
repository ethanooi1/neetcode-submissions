class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == '+':
                x = int(stack[-1])
                y = int(stack[-2])
                stack.append(str(x + y))
                continue
            elif operations[i] == 'D':
                stack.append(str(int(stack[-1]) * 2))
                continue
            elif operations[i] == 'C':
                stack.remove(stack[-1])
                continue
            stack.append(operations[i])
        
        sum = 0
        for n in range(len(stack)):
            sum += int(stack.pop())
        
        return sum
