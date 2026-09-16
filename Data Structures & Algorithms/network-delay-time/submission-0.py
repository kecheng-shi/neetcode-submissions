class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dict = defaultdict(list)

        for u, v, w in times:
            dict[u].append([v, w])

        dist = {node:float("inf") for node in range(1, n + 1)}

        def dfs(node, time):
            if time >= dist[node]:
                return
            
            dist[node] = time
            for next_node, travel_time in dict[node]:
                dfs(next_node, time + travel_time)

        dfs(k, 0)
        res = max(dist.values())
        return res if res < float("inf") else -1