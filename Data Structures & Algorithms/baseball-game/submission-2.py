class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for n in operations:
            if n == '+':
                stack.append(stack[-2] + stack[-1])
            elif n == 'D':
                stack.append(stack[-1] * 2)
            elif n == 'C':
                stack.pop()
            else:
                stack.append(int(n))
        return sum(stack)