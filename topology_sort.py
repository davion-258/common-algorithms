# Kahn's algorithm
from typing import List

def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
    g = [[] for _ in range(n)]
    in_degree = [0] * (n)
    q = []

    def build_graph():
        visited = [False] * (n)
        for nex, prev in prerequisites:
            g[prev].append(nex)
            in_degree[nex] += 1
            visited[nex] = True
        q.extend([node for node in range(n) if in_degree[node] == 0])            
    
    build_graph()
    ans = []
    learned = [False] * (n)
    while q:
        ans.extend(q)
        new_q = []
        for node in q:
            learned[node] = True
            for nei in g[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    new_q.append(nei)
        q = new_q
    return ans if len(ans) == n else []