# Problem: https://leetcode.com/problems/path-with-maximum-probability/description/
import heapq
from collections import defaultdict
from typing import List

def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    # Build graph with weight (succProb)
    g = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        g[u].append((succProb[i], v))
        g[v].append((succProb[i], u))
    
    # Init distance (probs)
    probs = [0] * 10001
    probs[start_node] = 1

    priority_queue = [(-1, start_node)]
    while priority_queue:
        # Retrieve the current shortest node
        prob, node = heapq.heappop(priority_queue)
        if node == end_node:
            return -prob
        
        # Traverse the neighbors
        for nei_prob, nei_node in g[node]:
            # Calculate distance from start to neighbor
            prob_to_nei = -prob * nei_prob
            # Update if the new distance is less than the current distance
            # then push to the priority queue
            if probs[nei_node] < prob_to_nei:
                probs[nei_node] = prob_to_nei
                heapq.heappush(priority_queue, (-prob_to_nei, nei_node))
    return 0