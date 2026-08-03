class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxInRange = -11000


        l = 0
        seen = defaultdict(int)
        res = []
        
        if k > len(nums):
            for num in nums:
                maxInRange = max(maxInRange, num)
            return [maxInRange]

        for r, val in enumerate(nums):
            seen[val] += 1
            maxInRange = max(maxInRange, int(val))

            if r - l + 1 == k:

                # add a check where if maxInRange == l and seen[maxInRange] == 1, check for new max 
                if maxInRange in seen:
                    res.append(maxInRange)
                else: 
                    maxInRange = -11000
                    for key in seen:
                        maxInRange = max(maxInRange, key)
                    res.append(maxInRange)
                
                if seen[nums[l]] == 1:
                    seen.pop(nums[l])
                else: 
                    seen[nums[l]] -= 1
                l += 1
            
        return res


        