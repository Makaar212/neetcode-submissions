class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # iterate through numCourses with a for loop, if it's not in prereqs then don't run dfs
        # and js append to res, if it is in preqs, then run dfs on that and see if every prereq is an 
        # actual class that can be taken

        preMap = defaultdict(list)
        seen = set()
        pres = set()
        presSeen = set()
        res = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            pres.add(pre)

        def dfs(crs):
            if crs in seen:
                return False
            if preMap[crs] == []:
                if crs not in presSeen:
                    res.append(crs)
                    presSeen.add(crs)
                return True

            seen.add(crs)
            for p in preMap[crs]:
                if not dfs(p):
                    return False
            preMap[crs] = []
            seen.remove(crs)
            if crs not in presSeen:
                presSeen.add(crs)
                res.append(crs)

            return True
        
        for crs in range(numCourses):
            if crs in pres:
                continue
            elif crs not in preMap:
                res.append(crs)
            elif crs in preMap and dfs(crs):
                continue
            else:
                return []
        return res