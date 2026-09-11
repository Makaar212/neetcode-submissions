class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # output: distinct combination of all possible letter combinations the digits can reperesent

        # input: string of digits

        # ideas:
            # hashmap for every digit

        # for evey digit in digits
        # add 
        # dfs 
        # pop
        # get number number
        # dfs
        # pop
        #get new number
        #dfs
        # pop
        digitKey = {
            "2" : ["a", "b","c"],
            "3" : ["d", "e","f"],
            "4" : ["g", "h","i"],
            "5" : ["j", "k","l"],
            "6" : ["m", "n","o"],
            "7" : ["p", "q","r","s"],
            "8" : ["t", "u","v"],
            "9" : ["w", "x","y","z"]
        }
        res = []
        # base case, when i >=len digits
        def dfs(i, cur):
            if i >= len(digits):
                res.append(''.join(cur))
                return
            
            for val in digitKey[digits[i]]:
                cur.append(val)
                dfs(i + 1, cur)
                cur.pop()
        dfs(0, [])

        return res