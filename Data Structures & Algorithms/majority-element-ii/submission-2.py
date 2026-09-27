class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = []
        for num in freq:
            if freq[num] > (len(nums) // 3):
                res.append(num)
        return res