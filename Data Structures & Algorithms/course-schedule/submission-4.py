class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this is a directed graph problem 
        # how do i know?
        # to take 0 you must take 1, 0 -> 1

        # for this problem we need to detect cycles
        # we also need to make an adjacency list

        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        cycle = set()

        def dfs(node):
            if node in cycle:
                return False
            if preMap[node] == []:
                return True
            
            cycle.add(node)
            for pre in preMap[node]:
                if not dfs(pre):
                    return False
            cycle.remove(node)
            preMap[node] = []
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True