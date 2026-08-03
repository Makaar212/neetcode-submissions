class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            num = temperatures[i]
            while stack and num > stack[-1][0]:
                stackVal, stackInd = stack.pop()
                res[stackInd] = i - stackInd 
            stack.append([num, i])
        return res