class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for string in strs:
            sortedString = ''.join(sorted(string))
            myDict[sortedString].append(string)
        
        return list(myDict.values())
