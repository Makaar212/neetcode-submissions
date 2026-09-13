class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        seen = set()
        for crs, preq in prerequisites:
            preMap[crs].append(preq)
        def dfs(crs):
            if crs in seen:
                return False
            if preMap[crs] == []:
                return True

            seen.add(crs)
            for prereq in preMap[crs]:
                if not dfs(prereq):
                    return False
            preMap[crs] = []
            seen.remove(crs)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        