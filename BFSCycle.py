from collections import defaultdict
from typing import DefaultDict

class Node:
	def __init__(self, number: int):
			self.number = number
			self.Visited = True
			self.Elos = {}
	
	def addElo(self, nextNode):
		self.Elos[len(self.Elos)] = (Elo(nextNode))

	def printElos(self):
		print(f"{self.number}-------->", end="")
		for i in self.Elos:
			if i == len(self.Elos) - 1:
				print(f"{self.Elos[i].childNode.number}")
			else:
				print(f"{self.Elos[i].childNode.number}-------->", end="")
		print("")

class Elo:
	def __init__(self, childNode: Node):
		self.childNode = childNode
		self.Visited = 0

	def setVisited(self, status: int):
		self.Visited = status

class Grafo:
	def __init__(self) -> None:
		self.Nodes = defaultdict(Node)

	def addNode(self, node: Node):
		self.Nodes.update({node.number: node})

	def addElo(self, currentNode: Node, nextNode: Node): # This is a direcioned Elo, possible fix: make the 2 nodes share the same elo 

		if currentNode.number in self.Nodes:
			currentNode = self.Nodes.get(currentNode.number)
		else:
			self.addNode(currentNode)

		if nextNode.number in self.Nodes:
			nextNode = self.Nodes.get(nextNode.number)
		else:
			self.addNode(nextNode)
		
		self.Nodes[currentNode.number].addElo(nextNode)
		# self.Nodes[nextNode.number].addElo(currentNode)
	def printGraph(self):
		for i in self.Nodes:
			if self.Nodes[i].Elos:
				self.Nodes[i].printElos()
	
	def BFS(self, root: int):
		if root not in self.Nodes:
			print("Não achado ponto de inicio.")
			return 0

		if root != list(self.Nodes)[0]:
			nodeList = {}
			for i in range(root, len(self.Nodes) + 1):
				if i in self.Nodes:
					nodeList.update({i - root + 1: self.Nodes[i]})

			
			for i in range(0, root):
				key = list(nodeList)[-1] + 1

				if i in self.Nodes:
					nodeList.update({key: self.Nodes[i]})

		for i in nodeList:
			nodeList[i]



g = Grafo()

g.addElo(Node(0), Node(1))

g.addElo(Node(1), Node(2))
g.addElo(Node(1), Node(3))

g.addElo(Node(2), Node(1))
g.addElo(Node(2), Node(3))
g.addElo(Node(2), Node(4))
g.addElo(Node(2), Node(5))

g.addElo(Node(3), Node(1))
g.addElo(Node(3), Node(2))
g.addElo(Node(3), Node(5))
g.addElo(Node(3), Node(7))
g.addElo(Node(3), Node(8))

g.addElo(Node(4), Node(2))
g.addElo(Node(4), Node(5))

g.addElo(Node(5), Node(3))
g.addElo(Node(5), Node(2))
g.addElo(Node(5), Node(4))
g.addElo(Node(5), Node(6))

g.addElo(Node(6), Node(5))

g.addElo(Node(7), Node(3))
g.addElo(Node(7), Node(8))

g.addElo(Node(8), Node(3))
g.addElo(Node(8), Node(7))

g.addElo(Node(9), Node(10))
g.addElo(Node(10), Node(9))
g.printGraph()

g.BFS(4)
# g.addElo2Nodes(g.Nodes[0], g.Nodes[1])
