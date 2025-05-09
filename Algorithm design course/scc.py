'''student groups - scc'''

from collections import defaultdict

def kosaraju_scc(graph, vertices):
    def DFS(node, visited, dfs_stack):

        visited[node] = True
        for neighbors in graph[node]:
            if not visited[neighbors]:
                DFS(neighbors, visited, dfs_stack)
        dfs_stack.append(node)

    def REVERSE_GRAPH():

        reversed_graph = defaultdict(list)
        for nodes in graph:
            for neighbor in graph[nodes]:
                reversed_graph[neighbor].append(nodes)
        return reversed_graph

    def SCC_DFS(node, visited, scc):

        visited[node] = True
        scc.append(node)
        for neighbors in reversed_graph[node]:
            if not visited[neighbors]:
                SCC_DFS(neighbors, visited, scc)

    visited = (vertices + 1) * [False]
    stack = []
    for nodes in range(1, vertices + 1):
        if not visited[nodes]:
            DFS(nodes, visited, stack)
    reversed_graph = REVERSE_GRAPH()
    visited = (vertices + 1) * [False]
    student_teams = []
    while stack:
        nodes = stack.pop()
        if not visited[nodes]:
            scc = []
            SCC_DFS(nodes, visited, scc)
            student_teams.append(scc)
    return student_teams

v, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

print(len(kosaraju_scc(graph, v)))
