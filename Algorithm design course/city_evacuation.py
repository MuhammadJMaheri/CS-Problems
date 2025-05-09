'''city evacuation problem'''

from collections import defaultdict, deque

n, m = map(int, input().split())

graph = defaultdict(list)
residual_graph = [[0] * (n+1) for _ in range(n+1)]

def addEdge(u, v, w):

    global graph , residual_graph
    graph[u].append(v)
    residual_graph[u][v] = w

for _ in range(m):
    u, v, w = map(int, input().split())
    addEdge(u, v, w)

def BFS(r_graph, parent, s, t):

    visited = len(r_graph) * [False]
    queue = deque()
    queue.append(s)
    visited[s] = True
    while queue:
        U = queue.popleft()
        for index, value in enumerate(r_graph[U]):
            if visited[index] is False and value > 0:
                visited[index] = True
                parent[index] = U
                queue.append(index)
    return bool(visited[t])

def FORD_F(s, t):

    global residual_graph
    parent = [-1] * (t+1)
    flow_max = 0
    while BFS(residual_graph, parent, s, t):
        path_flow = float("Inf")
        s_ = t
        while s_ != s:
            path_flow = min(path_flow, residual_graph[parent[s_]][s_])
            s_ = parent[s_]
        flow_max = flow_max + path_flow
        V = t
        while V != s:
            u = parent[V]
            residual_graph[u][V] -= path_flow
            residual_graph[V][u] += path_flow
            V = parent[V]
    return flow_max

#max_people = FORD_F(1, n)
print(f"{FORD_F(1, n)}")
