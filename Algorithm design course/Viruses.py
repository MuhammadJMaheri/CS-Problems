from enum import Enum

class Color(Enum):
    white = 0
    gray = 1
    black = 2

class Edge:
    def __init__(self, node1, node2, weight1, weight2):
        self.node1 = node1
        self.node2 = node2
        self.weight1 = weight1
        self.weight2 = weight2

class Node:
    def __init__(self, node_id):
        self.ID = node_id
        self.parent = None
        self.color = Color.white
        self.adj = []

def find_path(node1, node2, max_s):
    node1.color = Color.gray
    i = 0
    while i < len(node1.adj):
        if node1.adj[i].node1 == node2 or node1.adj[i].node2 == node2:
            if max_s is None or max_s.weight2 < node1.adj[i].weight2:
                max_s = node1.adj[i]
            return True
        else:
            if node1.adj[i].node1 == node1:
                if node1.adj[i].node2.color == Color.white:
                    if find_path(node1.adj[i].node2, node2, max_s):
                        if max_s is None or max_s.weight2 < node1.adj[i].weight2:
                            max_s = node1.adj[i]
                        return True
            else:
                if node1.adj[i].node1.color == Color.white:
                    if find_path(node1.adj[i].node1, node2, max_s):
                        if max_s is None or max_s.weight2 < node1.adj[i].weight2:
                            max_s = node1.adj[i]
                        return True
        i += 1
    node1.color = Color.black
    return False

def common_parent(node1, node2):
    parents1 = []
    while node1 is not None:
        parents1.append(node1)
        node1 = node1.parent
        if node1 in parents1:
            break

    parents2 = []
    in_a_tree = False
    while node2 is not None:
        if node2 in parents1:
            in_a_tree = True
            break
        if node2 in parents2:
            break
        parents2.append(node2)
        node2 = node2.parent

    if not in_a_tree:
        union_tree(parents1, parents2)

    return in_a_tree

def union_tree(parents1, parents2):
    if len(parents1) >= len(parents2):
        j = 0
        while j < len(parents1) - 1:
            parents1[j].parent = parents1[-1]
            j += 1

        j = 0
        while j < len(parents2):
            parents2[j].parent = parents1[-1]
            j += 1
    else:
        j = 0
        while j < len(parents1):
            parents1[j].parent = parents2[-1]
            j += 1

        j = 0
        while j < len(parents2) - 1:
            parents2[j].parent = parents2[-1]
            j += 1

if __name__ == "__main__":
    VE = input().split()
    V = int(VE[0])
    E = int(VE[1])
    GS = input().split()
    G = int(GS[0])
    S = int(GS[1])

    edges = []
    graph = [Node(i) for i in range(V)]

    i = 0
    while i < V:
        graph[i] = Node(i)
        i += 1

    j = 0
    while j < E:
        edge = input().split()
        edges.append(Edge(graph[int(edge[0]) - 1], graph[int(edge[1]) - 1], int(edge[2]), int(edge[3])))
        j += 1

    edges1 = sorted(edges, key=lambda x: x.weight1)
    edge_mst = []
    min_s = 0
    final_weight = float('inf')

    k = 0
    while k < E:
        if common_parent(edges1[k].node1, edges1[k].node2):
            remove = None
            l = 0
            while l < V:
                graph[l].color = Color.white
                l += 1

            find_path(edges1[k].node1, edges1[k].node2, remove)

            if remove.weight2 > edges1[k].weight2:
                edge_mst.append(edges1[k])
                edge_mst.remove(remove)
                remove.node1.adj.remove(remove)
                remove.node2.adj.remove(remove)
                edges1[k].node1.adj.append(edges1[k])
                edges1[k].node2.adj.append(edges1[k])
        else:
            edge_mst.append(edges1[k])
            edges1[k].node1.adj.append(edges1[k])
            edges1[k].node2.adj.append(edges1[k])

        if len(edge_mst) == V - 1:
            min_val = max(edge_mst, key=lambda x: x.weight2).weight2
            if final_weight > min_val * S + edges1[k].weight1 * G:
                final_weight = min_val * S + edges1[k].weight1 * G

        k += 1

    if final_weight == float('inf'):
        print(-1)
    else:
        print(final_weight)
