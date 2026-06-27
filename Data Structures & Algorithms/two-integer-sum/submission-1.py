class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict()

        for i, value in enumerate(nums): 
            if target - value in seen:
                partner = target - value
                return [seen[partner], i]
            else:
                seen[value] = i
        
        
                
        
        