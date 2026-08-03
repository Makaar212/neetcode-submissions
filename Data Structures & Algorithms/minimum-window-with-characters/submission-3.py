class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="": return ""

        # create a counter for T 
        countT, seen = defaultdict(int), defaultdict(int)

        for c in t:
            countT[c] += 1
        # create variables for need, have, seen vars, l, res, and resLen
        have, need = 0, len(countT)

        l, res, resLen = 0, [-1, -1], float('inf')
        # loop through s
        for r in range(len(s)):
            c = s[r]

            # add c to seen counter
            seen[c] += 1

            # if c in need and seen[c] >= need[c]
            if c in countT and seen[c] == countT[c]:
                # increment have by 1
                have += 1

            # while have == need
            while have == need:
                if r - l + 1 < resLen:
                # update resLen accordingly (is this len shorter than the other length?)
                    # if so update res and resLen
                    res = [l, r]
                    resLen = r - l + 1
                # decrement seen[s[l]]
                leftChar = s[l]
                seen[leftChar] -= 1



                # check if have still equals need
                if leftChar in countT and seen[leftChar] < countT[leftChar]:
                    have -= 1

                # move l up 1
                l += 1

        # return "" if res is empty else return s[res[0] : res[1] + 1] 
        return "" if res[0] == -1 else s[res[0]: res[1] + 1]