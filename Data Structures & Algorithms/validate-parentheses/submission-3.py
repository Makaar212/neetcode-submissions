class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        validator = {'(' : ')', '{' : '}', '[' : ']' }
        for c in s:
            if c in validator:
                stack.append(c)
            else:
                if not stack:
                    return False
                if validator[stack.pop()] != c:
                    return False

        if stack:
            return False
        return True


        