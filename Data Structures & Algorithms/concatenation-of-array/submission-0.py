class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [x for x in nums] * 2
        return res