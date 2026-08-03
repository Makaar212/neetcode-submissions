class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        sortedNums = sorted(nums)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = sortedNums[i] + sortedNums[l] + sortedNums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                elif sum == 0:
                    if (sortedNums[i], sortedNums[l], sortedNums[r]) not in seen:
                        result.append([sortedNums[i], sortedNums[l], sortedNums[r]])
                        seen.add((sortedNums[i], sortedNums[l], sortedNums[r]))
                    l += 1
        return result