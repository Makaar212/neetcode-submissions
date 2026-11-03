class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                first = stack.pop()
                print("Double op: " , first)
                stack.append(first)
                stack.append(first * 2)
            elif op == "+":
                first, second = stack.pop(), stack.pop()
                stack.append(second)
                stack.append(first)
                print("Addition op: ", first, " ", second)
                stack.append(first + second)
            else: 
                stack.append(int(op))

        return sum(stack)