class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = Counter(nums)
        result = []
        currentLargest = -1
        currentKey = -1
        for i in range(k):

            for key in myDict:
                if myDict[key] > currentLargest:
                    currentLargest = myDict[key]
                    currentKey = key
            result.append(currentKey)
            del myDict[currentKey]
            currentKey = -1
            currentLargest = -1

        return result
            
            
        