from collections import defaultdict
from typing import DefaultDict

class Node:
	def __init__(self, number):
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

		
		queque = []
		for i in nodeList:
			Layer = 'INF'
			queque.append(nodeList[i])
			while queque:
				currNode = queque.pop(0)
				currNode.Visited = True

				for j in currNode.Elos:

					if currNode.Elos[j].Visited == 0:
						currNode.Elos[j].Visited = 1
						currNode.Elos[j].childNode.Elos[currNode.number].Visited = 1

						currNode.Elos[j].childNode.Visited = True
						queque.append(currNode.Elos[j].childNode)

						
		for i in nodeList:
			print(f"{nodeList[i].number}: {nodeList[i].Visited}")

g = Grafo()