from typing import *
import heapq


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    adj_edges = [None]*n

    for edge in edges:
        if adj_edges[edge[0]] != None:
            adj_edges[edge[0]].append(edge[1:3])
        else:
            adj_edges[edge[0]] = [edge[1:3]]

        if adj_edges[edge[1]] != None:
            adj_edges[edge[1]].append([edge[0], edge[2]])
        else:
            adj_edges[edge[1]] = [[edge[0], edge[2]]]

    def dijkstra(edges: List[List[int]], start: int, N: int):
        vis = N*[False]
        dist = N*[float('inf')]
        dist[start] = 0

        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            cur_dist, cur_vertiec = heapq.heappop(pq)
            vis[cur_vertiec] = True
            if edges[cur_vertiec]:
                for next_ver, w in edges[cur_vertiec]:
                    if vis[next_ver]:
                        continue
                    # 這裡要注意 用dist[cur_vertiec] 不可以直接用cur_dist
                    cur_dist = dist[cur_vertiec]+w
                    if cur_dist < dist[next_ver]:
                        dist[next_ver] = cur_dist
                        heapq.heappush(pq, (cur_dist, next_ver))
        print(dist)
        return dist
    ans = None
    min_neighbors = float('inf')
    for vertice in range(n):
        neighbors = 0
        for dist in dijkstra(adj_edges, vertice, n):
            if dist <= distanceThreshold:
                neighbors += 1
        if neighbors <= min_neighbors:
            ans = vertice
            min_neighbors = neighbors
    return ans


# findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]],distanceThreshold=3)
# findTheCity(n=5, edges=[[0, 1, 2], [0, 4, 8], [1, 2, 3], [
#             1, 4, 2], [2, 3, 1], [3, 4, 1]], distanceThreshold=2)
findTheCity(n=6,
edges=[[2,3,7],[2,5,8],[0,2,8],[4,5,5],[1,5,10],[3,4,3],[0,5,9],[1,2,1]],
distanceThreshold= 3269)
# def dijks():
