import heapq
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # turn into adjacent list
    adj = [None]*n
    for time in times:
        if adj[time[0]-1] != None:
            adj[time[0]-1].append([time[1]-1, time[2]])
        else:
            adj[time[0]-1] = [[time[1]-1, time[2]]]

    # vertice visted or not
    vis = [False]*n
    # shoetest path for vertice
    dist = [float('inf')]*n
    dist[k-1] = 0
    # shortest path
    path=[None]*n

    pq = []
    # use pq to make sure you walk on the shortest way to vertice
    # then you can ignore the vertice which have been visited
    heapq.heappush(pq, (0, k-1))
    while pq:
        #   get the short path from pq
        cur_dist, node = heapq.heappop(pq)
        vis[node] = True
        # if vertice exist edge
        if adj[node]:
            # iter over vertice's connected vertice
            for edge, w in adj[node]:
                # if vertice visited pass
                if vis[edge]:
                    continue
                # the path sum for next vertice
                cur_dist = dist[node]+w
                # store the shortest path for connected vertice
                if cur_dist < dist[edge]:
                    dist[edge] = cur_dist
                    heapq.heappush(pq, (cur_dist, edge))
                    path[node]=edge

    optimal_path=[k]
    walk=path[k-1]

    while walk:
        optimal_path.append(walk+1)
        walk=path[walk]

    print(optimal_path,dist)


# example imput
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1],[4,2,1],[4,1,5]]
n = 4
k = 2

print(networkDelayTime(times, n, k))
