from collections import defaultdict
from typing import DefaultDict
import math
import random
import time

class Node:
	def __init__(self, name):
			self.Name = name
			self.Layer = math.inf
			self.Visited = False
			self.Elos = {}
	
	def addElo(self, nextNode):
		self.Elos.update({nextNode.Name: Elo(nextNode)})

	def searchInElos(self, nodeNumber):
		if nodeNumber in self.Elos:
			return self.Elos.get(nodeNumber)

	def printElos(self):
		strReturn = ""
		strReturn += f"{self.Name}-------->"
		for i in self.Elos:
			if i == list(self.Elos)[-1]:
				strReturn += f"{self.Elos[i].childNode.Name}"
			else:
				strReturn += f"{self.Elos[i].childNode.Name}-------->"
		strReturn += "\n"
		return(strReturn)
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

	def BFS(self, root: int):
		if root not in self.Nodes:
			print("Não achado ponto de inicio.")
			return 0

		if root != list(self.Nodes)[0]:
			nodeDic = {}
			nodeDic[root] = self.Nodes[root]

			for x in self.Nodes:
				if x != root:
					nodeDic[x] = self.Nodes[x]
		else:
			nodeDic = self.Nodes

		queque = []
		for i in nodeDic:

			queque.append(nodeDic[i])

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

						# if currNode.Name in currNode.Elos[j].childNode.Elos:
						# 	currNode.Elos[j].childNode.Elos[currNode.Name].Visited = 1
					
						currNode.Elos[j].childNode.Visited = True
						currNode.Elos[j].childNode.Layer = currNode.Layer + 1

						queque.append(currNode.Elos[j].childNode)

					elif currNode.Elos[j].childNode.Visited and currNode.Elos[j].Visited == 0:
						currNode.Elos[j].Visited = 2
		self.BFSPass = True

	def printGraph(self):
		strReturn = ""
		for i in self.Nodes:
			if self.Nodes[i].Elos:
				strReturn += self.Nodes[i].printElos()
		return strReturn

	def printLayers(self):
		print("Layers: \n")
		for x in self.Nodes:
				print(f"  {self.Nodes[x].Name}: {self.Nodes[x].Layer}")
		print("\n")

	def printVisited(self):
		for i in self.Nodes:
			print(f"{self.Nodes[i].Name}: ")
			for j in self.Nodes[i].Elos:
				print(f"  {self.Nodes[i].Name} - {self.Nodes[i].Elos[j].childNode.Name}: {self.Nodes[i].Elos[j].Visited}")