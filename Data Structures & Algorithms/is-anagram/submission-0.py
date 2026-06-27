class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        tHash = defaultdict(int)
        sHash = defaultdict(int)


        for i in range(len(s)):
            tHash[t[i]] += 1
            sHash[s[i]] += 1

        
        return tHash == sHash
        
        