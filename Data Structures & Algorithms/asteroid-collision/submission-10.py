class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # iterate through nums
        stack = []
        for num in asteroids:
            # if positive
            if num > 0 or not stack or stack[-1] < 0:
                stack.append(num)
            else:            
                while stack and stack[-1] > 0 and  abs(num) > abs(stack[-1]):
                    
                    stack.pop()
                if stack and stack[-1] > 0:
                    if stack and stack[-1] == abs(num):
                        stack.pop()
                        continue
                    if stack and abs(stack[-1]) > abs(num):
                        continue
                stack.append(num)
                
        return stack
            # if negative
            

        # if reaching negative and stack 

            # pop from stack while negative num is greater 
            # if they're equal then pop once and be done
            # if positive number is greater than just destroy the negative and move on 