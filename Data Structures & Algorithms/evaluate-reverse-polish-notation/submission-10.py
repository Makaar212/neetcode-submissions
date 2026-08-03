class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for toke in tokens:
            if toke == "+":
                stack.append(stack.pop() + stack.pop())
            elif toke == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif toke == "*":
                stack.append(stack.pop() * stack.pop())
            elif toke == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(toke))

        return stack[0]


        