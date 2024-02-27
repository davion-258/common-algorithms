# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from ast import List

MAX = 1_000_000

# O(K*(N+E))
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Init distance
        costs = [MAX] * n
        costs[src] = 0

        # Loop for number of intermediate nodes
        for stops in range(k + 1):
            temp = costs.copy()
            for u, v, cost in flights:
                # if cost to u, then update cost to v = costs[u] + cost_u_to_v
                if costs[u] != MAX:
                    temp[v] = min(temp[v], costs[u] + cost)
            costs = temp
        
        return costs[dst] if costs[dst] != MAX else -1