from typing import *
import copy
import collections
import heapq
def findItinerary(tickets: List[List[str]]) -> List[str]:
    sort_path = collections.defaultdict(list)
    for a, b in tickets:
        tmp=sort_path[a]
        heapq.heappush(tmp,b)
        sort_path[a]=tmp
    # 1. The nodes which have odd degrees (int and out) are the entrance or exit. In your example it's JFK and A.
    # 2. If there are no nodes have odd degrees, we could follow any path without stuck until hit the last exit node
    # 3. The reason we got stuck is because that we hit the exit
    route=[]
    def dfs(start):
        while sort_path[start]:
            dfs(heapq.heappop(sort_path[start]))
        # get to exit point
        route.append(start)
    dfs('JFK')
    
    return route

    # straight forward DFS
    
    # sort_path = collections.defaultdict(list)
    # for a,b in sorted(tickets):
    #     sort_path[a] += b,
    
    # start='JFK'
    # ans=[start]
    # def dfs(paths,start,n,N):
    #     total=0
    #     for _,v in paths.items():
    #         total+=len(v)
    #     if n==N-1:
    #         return [paths[start][0]]
    #     if start not in paths or not paths[start] :
    #         return
        
    #     for idx,path in enumerate(paths[start]):
    #         if path not in paths:
    #             continue
    #         cur_path=copy.deepcopy(paths)
    #         cur_path[start]=cur_path[start][:idx]+cur_path[start][idx+1:]
    #         ans_path=dfs(cur_path,path,n+1,N)
    #         if ans_path:
    #             return [path]+ans_path
    # N=len(tickets)
    # ans+=dfs(sort_path,start,0,N)


# findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
# findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
# findItinerary([["AXA","AUA"],["BNE","ANU"],["EZE","ANU"],["TIA","JFK"],["TIA","BNE"],["ANU","BNE"],["BNE","AUA"],["BNE","ADL"],["AXA","ADL"],["EZE","AUA"],["AUA","AXA"],["ADL","AXA"],["ADL","TIA"],["JFK","ANU"],["EZE","JFK"],["JFK","AUA"],["BNE","EZE"],["TIA","ANU"],["TIA","AUA"],["JFK","TIA"],["EZE","ANU"],["AXA","JFK"],["AUA","OOL"],["AUA","AXA"],["ANU","BNE"],["ANU","EZE"],["ANU","TIA"],["JFK","EZE"],["ADL","ANU"],["AXA","BNE"],["BNE","ADL"],["ANU","EZE"],["ANU","JFK"],["BNE","AUA"],["ANU","AUA"],["ANU","AXA"],["TIA","BNE"],["AUA","EZE"],["JFK","ANU"],["AXA","TIA"],["EZE","ANU"],["AUA","BNE"],["AUA","AXA"],["AUA","TIA"]])