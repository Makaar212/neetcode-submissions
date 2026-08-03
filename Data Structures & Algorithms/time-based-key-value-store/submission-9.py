class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append( tuple([timestamp, value]))

    def get(self, key: str, timestamp: int) -> str:
        
        # if the key doesn't exist yet, return "" 
        if not self.storage[key]:
            return ""
        valueList = self.storage[key]

        # If the timestamp is lower than our current amount return ""
        if timestamp < valueList[0][0]:
            return  ""
        
        # if the timestamp is greater than the highest value return that
        if timestamp >= valueList[-1][0]:
            return valueList[-1][1]

        # Binary search to find the timestamp otherwise
        l, r = 0, len(valueList) - 1
        best = ""
        bestNextThing = ""
        while l <= r:
            m = (l + r) // 2 
            if  valueList[m][0] == timestamp:
                return valueList[m][1]
            if valueList[m][0] < timestamp:
                bestNextThing = valueList[m][1]
                l = m + 1
            else:
                r = m - 1
        return bestNextThing if not best else best


        


