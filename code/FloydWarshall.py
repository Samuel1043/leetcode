from typing import List


inf = float('inf')


def FloydWarshall(dp, dp_next, n):
    """[summary]
    get the optimal path for i->j routing through k
    Args:
        dp (List[List[]]): the optimal path between two vertice, ex: dp[i,j] optimal path from i->j
        dp_next (List[List[]]): the next vertice to go through for the optimal path for two vertice
        n (int): number of vertice
    """
    for i in range(n):
        for j in range(n):
            # if vertice didn't point to itself don't need to calcaulate
            # if i==j:
                # continue
            for k in range(n):
                if (dp[i][k]+dp[k][j] < dp[i][j]):
                    dp[i][j] = dp[i][k]+dp[k][j]
                    dp_next[i][j] = dp_next[i][k]
    return dp, dp_next


def propagateNegativeCycle(dp, dp_next, n):
    """[summary]
        to detect negative cycle run Floyd's algorithm again 
        because the optimal path should be set for calling floyd once, 
        if calling floyd again cause some other route to be smaller 
        than the original path there is a negative cycle. 
    Args:
        dp (List[List[]]): the optimal path between two vertice, ex: dp[i,j] optimal path from i->j
        dp_next (List[List[]]): the next vertice to go through for the optimal path for two vertice
        n (int): number of vertice

    Returns:
        [dp,dp_next]: [description]
    """
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (dp[i][k]+dp[k][j] < dp[i][j]):
                    dp[i][j] = -inf
                    # the negative cycle edge
                    dp_next[i][j] = -1
    return dp, dp_next


def reconstructPath(dp, dp_next, start, end):
    """[summary]

    Args:
        dp (List[List[int]]): the shortest path from vertice to vertice
        dp_next (List[List[int]]): the next vertice to walk for the shortest path from vertice to vertice
        start (int): start vertice
        end (int): end vertice

    Returns:
        List[],None: the vertices that shortest path walk through
                        None if it's negative cycle, [] if no path exist
    """
    path = []
    # no path from start to end
    if dp[start][end] == inf:
        return []
    # initialize start vertice
    at = start
    # walk through the path
    while at != end:
        if at == -1:
            return None
        path.append(at)
        # got to the next shortest path vertice
        at = dp_next[at][end]

    if dp_next[at][end] == -1:
        return None
    path.append(at)
    return path


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    m = [[inf if i != j else 0 for i in range(n)] for j in range(n)]
    for edge in edges:

        m[edge[0]][edge[1]] = edge[2]

    def setup(m, n):
        dp = [[inf for _ in range(n)] for _ in range(n)]
        dp_next = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j] = m[i][j]
                if m[i][j] != inf:
                    dp_next[i][j] = j
        return dp, dp_next

    dp, dp_next = setup(m, n)

    dp, dp_next = FloydWarshall(dp, dp_next, n)
    dp, dp_next = propagateNegativeCycle(dp, dp_next, n)
    path = reconstructPath(dp, dp_next, 1, 3)

    print('shortest path: {} \n shortest path next vertice {}\
    \nshortest path from vertice 1->3 {}'.format(dp, dp_next, path))


findTheCity(n=4, edges=[[0, 1, 3], [1, 2, -10],
                        [2, 3, 4], [3, 1, 1]], distanceThreshold=3)
