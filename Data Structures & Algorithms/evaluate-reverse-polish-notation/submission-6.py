class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in ['+', '-', '*', '/']:
                if c == '+':
                    new = stack.pop()
                    stack.append(stack.pop() + new)
                elif c == '-':
                    new = stack.pop()
                    stack.append(stack.pop() - new)
                elif c == '*':
                    new = stack.pop()
                    stack.append(stack.pop() * new)
                else:
                    new = stack.pop()
                    stack.append(int(round(stack.pop() / new, 1)))
            else:
                stack.append(int(c))
        
        return stack[0]
        