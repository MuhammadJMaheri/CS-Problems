'''city piping problem'''

from collections import defaultdict

def DFS(total_nodes, undirected_edges_inner, visited, components_inner):

    for k in range(1, total_nodes + 1):
        if not visited[k]:
            output = []
            REC_DFS(k, undirected_edges_inner, visited, output)
            components_inner.append(output)

def REC_DFS(k, undirected_edges_inner, visited, output):

    output.append(k)
    neighbors = undirected_edges_inner[k]
    visited[k] = True
    for j in neighbors:
        if not visited[j]:
            REC_DFS(j, undirected_edges_inner, visited, output)

def CYCLIC_CHECK(nodes, component, adjacent):

    visited = (nodes + 1) * [False]
    rec_check = (nodes + 1) * [False]
    for k in component:
        if CYCLE_CHECK(k, component, visited, rec_check, adjacent):
            return True
    return False

def CYCLE_CHECK(i, component, visited, rec_check, adjacent):

    if rec_check[i]:
        return True
    if visited[i]:
        return False
    children = adjacent[i]
    visited[i] = True
    rec_check[i] = True
    for child in children:
        if CYCLE_CHECK(child, component, visited, rec_check, adjacent):
            return True
    rec_check[i] = False
    return False

def MIN_PIPES(components, total_nodes, adjacency):

    count = 0
    for component in components:
        if CYCLIC_CHECK(total_nodes, component, adjacency):
            count += len(component)
        else:
            count += len(component) - 1
    return count

no_cities, no_important_pipes = list(map(int, input().split()))
undirected_edges, directed_edges = defaultdict(list), defaultdict(list)
for i in range(1, no_cities + 1):
    directed_edges[i] = []
    undirected_edges[i] = []
for _ in range(no_important_pipes):
    p = list(map(int, input().split()))
    undirected_edges[p[0]].append(p[1])
    undirected_edges[p[1]].append(p[0])
    directed_edges[p[0]].append(p[1])
components = []

DFS(no_cities, undirected_edges, [False] * (no_cities + 1), components)
print(MIN_PIPES(components, no_cities, directed_edges))
