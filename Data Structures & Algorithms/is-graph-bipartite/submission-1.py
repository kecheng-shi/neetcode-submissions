class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        for start in range(n):
            if color[start] != 0:
                continue

            color[start] = 1
            stack = [start]

            while stack:
                node = stack.pop()

                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        stack.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        
        return True