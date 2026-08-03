class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p,s in zip(position, speed)]
        stack = []
        for p,s  in sorted(pairs)[::-1]: # Traverse through the sorted array backwards
            stack.append((target-p) / s) # append the time to target
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # check if time to target is greater than
                stack.pop()
        
        return len(stack)

