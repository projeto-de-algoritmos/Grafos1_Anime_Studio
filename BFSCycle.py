from collections import defaultdict
from typing import DefaultDict

class Node:
	def __init__(self, number: int):
			self.number = number
			self.Visited = False
			self.Elos = {}
	
	def addElo(self, nextNode):
		self.Elos[len(self.Elos)] = (Elo(nextNode))

	def printElos(self):
		for i in self.Elos:
			print(self.Elos[i].childNode.number)

class Elo:
	def __init__(self, childNode: Node):
			self.childNode = childNode
			self.Visited = False


class Grafo:
	def __init__(self) -> None:
			self.Nodes = defaultdict(Node)

	def addNode(self, node: Node):
			self.Nodes[node.number] = node

	def addElo(self, currentNode: Node, nextNode: Node):
		if currentNode.number in self.Nodes:
			currentNode = self.Nodes.get(currentNode.number)
		else:
			self.addNode(currentNode)
		
		if nextNode.number in self.Nodes:
			nextNode = self.Nodes.get(nextNode.number)
		else:
			self.addNode(nextNode)
		
		self.Nodes[currentNode.number].addElo(nextNode)

		




g = Grafo()


n1 = Node(1)

n1.addElo(Node(0))

n1.printElos()

print("Recreating")

n1.addElo(Node(1))

n1.printElos()

# g.addElo2Nodes(g.Nodes[0], g.Nodes[1])
