class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)

        for num, frequency in freq.items():
            if frequency > len(nums) // 2:
                return num
            