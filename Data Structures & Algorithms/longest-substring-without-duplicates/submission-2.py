class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        elif s == 1:
            return 1
        
        longest = 1
        l, r = 0,1
        seen = set()
        seen.add(s[l])
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(r - l + 1, longest)
            r += 1
        
        return longest
        