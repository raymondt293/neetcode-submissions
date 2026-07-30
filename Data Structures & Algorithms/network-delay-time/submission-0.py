class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v,w))

        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        while min_heap:
            w1, u = heapq.heappop(min_heap)

            if u in visited:
                continue
            
            visited.add(u)
            max_time = w1

            if len(visited) == n:
                return max_time
            
            for v, w2 in adj[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (w1 + w2, v))

        
        return max_time if len(visited) == n else -1
        