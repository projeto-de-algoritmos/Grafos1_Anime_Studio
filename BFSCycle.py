from collections import defaultdict
from typing import DefaultDict
import math
class Node:
	def __init__(self, number: int):
			self.number = number
			self.Layer = None
			self.Visited = False
			self.Elos = {}
	
	def addElo(self, nextNode):
		self.Elos.update({nextNode.number: Elo(nextNode)})

	def searchInElos(self, nodeNumber):
		if nodeNumber in self.Elos:
			return self.Elos.get(nodeNumber)

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
		self.BFSPass = False
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
		else:
			nodeList = self.Nodes
		
		queque = []
		Layer = 0
		for i in nodeList:

			# if Layer:
			# 	currNode.Layer = math.inf

			queque.append(nodeList[i])

			while queque:
				# for x in queque:
				# 	print(f"{x.number}, ", end="")
				# print("")
				currNode = queque.pop(0)

				if currNode.number == root:
					currNode.Layer = 0

				if not currNode.Visited:
					currNode.Visited = True

				for j in currNode.Elos:
					if currNode.Elos[j].childNode.Visited == 0:
						# print(f"CurrntNOde: {currNode.number}, CurrntChildNode: {currNode.Elos[j].childNode.number}")
						currNode.Elos[j].Visited = 1
						if currNode.number in currNode.Elos[j].childNode.Elos:
							currNode.Elos[j].childNode.Elos[currNode.number].Visited = 1
					
						currNode.Elos[j].childNode.Visited = True
						
						if currNode.Layer == None:
							currNode.Layer = math.inf
							currNode.Elos[j].childNode.Layer = math.inf
						else:
							currNode.Elos[j].childNode.Layer = currNode.Layer + 1

						queque.append(currNode.Elos[j].childNode)
					elif currNode.Elos[j].Visited == 0:
						currNode.Elos[j].Visited = 2
						


		for x in nodeList:
			print(f"{nodeList[x].number}: {nodeList[x].Layer}")
		self.BFSPass = True
	
	def printVisited(self):
		for i in self.Nodes:
			print(f"{self.Nodes[i].number}: ")
			for j in self.Nodes[i].Elos:
				print(f"  {self.Nodes[i].number} - {self.Nodes[i].Elos[j].childNode.number}: {self.Nodes[i].Elos[j].Visited}")

g = Grafo()



# g.addElo(Node(0), Node(1))

# g.addElo(Node(1), Node(0))
# g.addElo(Node(1), Node(2))

# g.addElo(Node(2), Node(1))
# g.addElo(Node(2), Node(3))

# g.addElo(Node(3), Node(0))

# g.addElo(Node(9), Node(8))
# g.addElo(Node(8), Node(9))

g.addElo(Node(0), Node(1))

g.addElo(Node(1), Node(0))
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
g.addElo(Node(10), Node(11))

g.addElo(Node(11), Node(10))
# g.printGraph()

g.BFS(0)

g.printVisited()
# g.addElo2Nodes(g.Nodes[0], g.Nodes[1])
