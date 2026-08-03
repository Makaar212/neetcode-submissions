class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = defaultdict(int), defaultdict(int)

        for c in t: 
            countT[c] += 1

        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = float("inf")
        l  = 0 
        
        for r, value in enumerate(s):
            window[value] += 1

            if value in countT and window[value] == countT[value]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1 
                    res = [l, r]
                
                leftChar = s[l]
                window[leftChar] -= 1
                
                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1
                
                l += 1
        
        return "" if res[0] == -1 else s[res[0]:res[1] + 1]
            