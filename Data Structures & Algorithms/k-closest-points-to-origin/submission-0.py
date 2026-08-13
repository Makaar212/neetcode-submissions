class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # For every point determine euclidean distance to origin, use tuples with euclidian distance
        # as the first value
        distance = []
        
        for x, y in points:
            distance.append(
                tuple([(math.sqrt(x**2 + y**2)), x, y])
            )

        # heapify the array
        heapq.heapify(distance)

        # while k add the points to res
        res = []
        while k:
            top = heapq.heappop(distance)
            res.append([top[1], top[2]])
            k -= 1

        # return res
        return res