class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        seen = set()

        for crs, preq in prerequisites:
            preMap[crs].append(preq)
        
        def dfs(crs):
            if crs in seen:
                return False
            if preMap[crs] == []:
                return True
            
            seen.add(crs)
            for p in preMap[crs]:
                if not dfs(p): return False
            preMap[crs] = []
            seen.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
