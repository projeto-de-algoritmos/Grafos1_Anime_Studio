from collections import defaultdict
from typing import DefaultDict
import math
class Node:
	def __init__(self, name):
			self.Name = name
			self.Layer = None
			self.Visited = False
			self.Elos = {}
	
	def addElo(self, nextNode):
		self.Elos.update({nextNode.Name: Elo(nextNode)})

	def searchInElos(self, nodeNumber):
		if nodeNumber in self.Elos:
			return self.Elos.get(nodeNumber)

	def printElos(self):
		print(f"{self.Name}-------->", end="")
		for i in self.Elos:
			if i == len(self.Elos) - 1:
				print(f"{self.Elos[i].childNode.Name}")
			else:
				print(f"{self.Elos[i].childNode.Name}-------->", end="")
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
		self.Nodes.update({node.Name: node})

	def addElo(self, currentNode: Node, nextNode: Node): # This is a direcioned Elo, possible fix: make the 2 nodes share the same elo 

		if currentNode.Name in self.Nodes:
			currentNode = self.Nodes.get(currentNode.Name)
		else:
			self.addNode(currentNode)

		if nextNode.Name in self.Nodes:
			nextNode = self.Nodes.get(nextNode.Name)
		else:
			self.addNode(nextNode)
		
		self.Nodes[currentNode.Name].addElo(nextNode)
		# self.Nodes[nextNode.Name].addElo(currentNode)
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
			print(self.Nodes)
			if type(root) not in [int, float]:
				Nroot = list(self.Nodes.keys()).index(root)
				# print(root)
			else:
				Nroot = root

			for i in range(Nroot, len(self.Nodes)):
				print(i)
				currnt = list(self.Nodes.keys())[i]
				print(currnt)
				if currnt in self.Nodes:
					print("Olas")

					nodeList.update({currnt: self.Nodes[currnt]})

			
			for i in range(0, Nroot):
				currnt = list(self.Nodes.keys())[i]
				print(currnt)
				if currnt in self.Nodes:
					nodeList.update({currnt: self.Nodes[currnt]})
		else:
			nodeList = self.Nodes
		
		print(nodeList)

		queque = []
		Layer = 0
		for i in nodeList:

			# if Layer:
			# 	currNode.Layer = math.inf

			queque.append(nodeList[i])

			while queque:
				# for x in queque:
				# 	print(f"{x.Name}, ", end="")
				# print("")
				currNode = queque.pop(0)

				if currNode.Name == root:
					currNode.Layer = 0

				if not currNode.Visited:
					currNode.Visited = True

				for j in currNode.Elos:
					if currNode.Elos[j].childNode.Visited == 0:
						# print(f"CurrntNOde: {currNode.Name}, CurrntChildNode: {currNode.Elos[j].childNode.Name}")
						currNode.Elos[j].Visited = 1
						if currNode.Name in currNode.Elos[j].childNode.Elos:
							currNode.Elos[j].childNode.Elos[currNode.Name].Visited = 1
					
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
			print(f"{nodeList[x].Name}: {nodeList[x].Layer}")
		self.BFSPass = True
	
	def printVisited(self):
		for i in self.Nodes:
			print(f"{self.Nodes[i].Name}: ")
			for j in self.Nodes[i].Elos:
				print(f"  {self.Nodes[i].Name} - {self.Nodes[i].Elos[j].childNode.Name}: {self.Nodes[i].Elos[j].Visited}")

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


# g.addElo(Node("Atk"), Node("MAPPA"))
# g.addElo(Node("MAPPA"), Node("Atk"))

g.BFS(5)

# print(g.Nodes["MAPPA"].Layer)

g.printVisited()
# g.addElo2Nodes(g.Nodes[0], g.Nodes[1])
