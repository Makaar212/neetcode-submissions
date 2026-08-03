class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        
        l = 0
        key = Counter(s1)
        seen = defaultdict(int)

        for r in range(len(s2)):        
            seen[s2[r]] += 1

            while r - l + 1 > len(s1):
                if seen[s2[l]] <= 1:
                     seen.pop(s2[l])
                else:
                    seen[s2[l]] -= 1
                l += 1
            
            if key == seen:
                return True
        return False