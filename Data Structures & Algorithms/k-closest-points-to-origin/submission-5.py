
class Solution:
    def dist(self, point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_idx_map: dict[float, list[int]] = {}
        distances = []

        # map each possible distance to a list of indices
        for i, point in enumerate(points):
            dist = self.dist(point)
            if not dist in distances: # figure out how to do with sets
                distances.append(dist)
                
            if dist in dist_idx_map.keys():
                dist_idx_map[dist].append(i)
            else:
                dist_idx_map[dist] = [i]

        # heapify list and get the top k distances, and points
        heapq.heapify(distances)
        top_k_points = []
        while len(top_k_points) < k:
            next_dist = heapq.heappop(distances)
            top_k_points.extend(
                [points[i] for i in dist_idx_map[next_dist]]
            )

        return top_k_points[:k]


        

        
            

        
        