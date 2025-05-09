from collections import defaultdict
n, m = (input()).split()
n = int(n)
m = int(m)
class graph:
	def __init__(self, vertices):
		self.vert = vertices
		self.graph = defaultdict(list)
	def edgeadd(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)
	def dfsl(self, v, visited):
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] is False:
				self.dfsl(i, visited)
	def isitconnected(self):
		visited = [False]*(self.vert)
		for i in range(self.vert):
			if len(self.graph[i]) != 0:
				break
		if i == self.vert-1:
			return True
		self.dfsl(i, visited)
		for i in range(self.vert):
			if visited[i] is False and len(self.graph[i]) > 0:
				return False
		return True
	def isiteuler(self):
		if self.isitconnected() is False:
			return 0
		else:
			odd = 0
			for i in range(self.vert):
				if len(self.graph[i]) % 2 != 0:
					odd += 1
			if odd == 0:
				return 2
			elif odd == 2:
				return 1
			elif odd > 2:
				return 0
	def result(self):
		res = self.isiteuler()
		if res == 0:
			print("NO")
		elif res == 1:
			print("YES")
		else:   
			print("YES")
g = graph(n)
for i in range(m):
    r, y = (input()).split()
    r = int(r) -1
    y= int(y) -1
    g.edgeadd(r, y)
g.result()