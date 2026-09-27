class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = set()
        for num in nums:
            if freq[num] > (len(nums) // 3):
                res.add(num)
        return list(res)