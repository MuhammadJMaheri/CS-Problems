from collections import defaultdict

def bfs(graph, match, dist, n, m):
   queue = []
   for u in range(n):
       if match[u] == -1:
           dist[u] = 0
           queue.append(u)
       else:
           dist[u] = float('inf')
   dist[n+m] = float('inf')

   while queue:
       u = queue.pop(0)
       if u != -1:
           for v in graph[u]:
               if dist[match[v]] == float('inf'):
                  dist[match[v]] = dist[u] + 1
                  queue.append(match[v])
   return dist[n+m] != float('inf')

def dfs(graph, match, dist, u, n):
   if u == -1:
       return True
   for v in graph[u]:
       if dist[match[v]] == dist[u] + 1 and dfs(graph, match, dist, match[v], n):
           match[v] = u
           match[u] = v
           return True
   dist[u] = float('inf')
   return False

def hopcroft_karp(graph, n, m):
   match = [-1]*(n + m)
   dist = [0]*(n + m)
   matching = 0
   while bfs(graph, match, dist, n, m):
       for u in range(n):
           if match[u] == -1 and dfs(graph, match, dist, u, n):
               matching += 1
   return matching, match[:n]

n, m = map(int, input().split())
graph = defaultdict(list)
for i in range(n):
   row = list(map(int, input().split()))
   for j in range(m):
       if row[j]:
           graph[i].append(n + j)
print(*hopcroft_karp(graph, n, m)[1])
