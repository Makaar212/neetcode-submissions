class MyStack:

    def __init__(self):
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)        
    
    
    def pop(self) -> int:
        temp = self.stack[-1]
        i, j = len(self.stack) - 1, len(self.stack) - 2

        for x in range(len(self.stack) - 1):
            if i < 0:
                break
            self.stack[i], self.stack[j] = self.stack[j], self.stack[i]
            i -= 1
            j -= 1

        return self.stack.popleft()
        

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return True if not self.stack else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()