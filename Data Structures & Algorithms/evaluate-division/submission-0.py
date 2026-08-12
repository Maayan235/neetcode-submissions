from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        # build the graph 
        for e in range(len(equations)):
            i, j = equations[e]
            weight = values[e]
            graph[i].append([j, weight])
            graph[j].append([i, 1 / weight])

        # brute force the graph - bfs/dfs
        output = list()

        for i, j in queries:
            if i not in graph or j not in graph:
                output.append(-1.0)
                continue

            queue = deque()
            queue.append([i, 1])
            res = -1 
            visited = set()
            visited.add(i)
            while queue:
                node, weight = queue.popleft()
                visited.add(node)
                if node == j:
                    res = weight
                    break

                for v, e in graph[node]:
                    if v not in visited:
                        visited.add(v)
                        queue.append([v, weight * e])
                
            output.append(res)

        return output 






        



        