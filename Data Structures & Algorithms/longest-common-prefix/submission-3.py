class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # brute force would be to iterate through every string, and see where theymatch up until they don't 
        # match anymore, 

        # we can do a hashmap approach where we     
        firstWord = strs[0]

        res = 0
        for i in range(len(firstWord)):
            c = firstWord[i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != c:
                    return firstWord[0:res ]
            res += 1
        return firstWord[0: res]

