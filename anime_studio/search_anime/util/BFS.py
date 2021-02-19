from collections import defaultdict
import math
import networkx as nx
import matplotlib.pyplot as plt
class Node:
	def __init__(self, name):
			self.Name = name
			self.Layer = math.inf
			self.Visited = False


class Elo:
	def __init__(self, parentNode: Node, childNode: Node):
		self.parentNode = parentNode
		self.childNode = childNode
		self.Visited = 0
		self.Layer = math.inf

	def setVisited(self, status: int):
		self.Visited = status


class Grafo:
	def __init__(self, isDirected: bool = False) -> None:
		self.Nodes = defaultdict(Node)
		self.Elos = []
		self.isDirected = isDirected	
		self.BFSPass = False
		

	def addNode(self, node: Node):
		self.Nodes.update({node.Name: node})
		
	def addElo(self, currentNode: Node, nextNode: Node):

		if currentNode.Name in self.Nodes:
			currentNode = self.Nodes.get(currentNode.Name)
		else:
			self.addNode(currentNode)

		if nextNode.Name in self.Nodes:
			nextNode = self.Nodes.get(nextNode.Name)
		else:
			self.addNode(nextNode)
		
		ElosList = []
		for i in self.Elos:
			ElosList.append((i.parentNode, i.childNode))

		if self.isDirected:
			if (currentNode, nextNode) not in ElosList:
				self.Elos.append(Elo(currentNode, nextNode))
		else:
			if (currentNode, nextNode) not in ElosList and (nextNode, currentNode) not in ElosList:
				self.Elos.append(Elo(currentNode, nextNode))
				self.Elos.append(Elo(nextNode, currentNode))
	
	def adjNodes(self, node: Node): 
		adjList = []

		for Elo in self.Elos:
			if Elo.parentNode.Name == node.Name and Elo.childNode.Name not in adjList:
				adjList.append(Elo.childNode)

		if adjList == []:
			return False

		return adjList

	def printElos(self, node:int):
		strReturn = ""

		if node in self.Nodes:
			strReturn += f"{self.Nodes[node].Name}"
			nodeList = self.adjNodes(self.Nodes.get(node))
			if nodeList:
				strReturn += "------->"
				for childNode in nodeList:
						if childNode != nodeList[-1]:
							strReturn += f"{childNode.Name}------->"
						else:
							strReturn += f"{childNode.Name}\n"
		else:
			print("Node não encontrado", end="")
		
		# print(strReturn)
		return strReturn
	
	def BFS(self, root):
		if root not in self.Nodes:
			print("Não achado ponto de inicio.")
			return False

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
				currNode = queque.pop(0)

				if currNode.Name == root:
					currNode.Layer = 0

				if not currNode.Visited:
					currNode.Visited = True

				for adjNode in self.adjNodes(currNode):
					if adjNode.Visited == 0:

						adjNode.Visited = 1

						adjNode.Visited = True
						adjNode.Layer = currNode.Layer + 1

						queque.append(adjNode)

					elif adjNode.Visited and adjNode.Visited == 0:
						adjNode.Visited = 2
		self.BFSPass = True

	def printGraph(self):
		strReturn = ""
		for node in self.Nodes:
			strReturn += self.printElos(self.Nodes[node].Name)
		return strReturn

	def printLayers(self):
		strReturn = f"Distacia o node {list(self.Nodes)[0]}\n"
		for x in self.Nodes:
				strReturn += f"  {self.Nodes[x].Name}: {self.Nodes[x].Layer}"

	def printVisited(self):
		for i in self.Nodes:
			print(f"{self.Nodes[i].Name}: ")
			for j in self.Nodes[i].Elos:
				print(f"  {self.Nodes[i].Name} - {self.Nodes[i].Elos[j].childNode.Name}: {self.Nodes[i].Elos[j].Visited}")

	def plotGraph(self, saveFileIn:str = "./search_anime/util/plot_grafos/"):
		dictNodes = {}
		elosList = []
		if type(list(self.Nodes)[0]) == int:
			for i in self.Nodes:
				tmp = self.Nodes[i].Name
				dictNodes.update({tmp: tmp})
		else:
			for index, node in enumerate(self.Nodes):
				dictNodes.update({index: self.Nodes[node].Name})
		for elo in self.Elos:
			elosList.append((elo.parentNode.Name, elo.childNode.Name))
		tmpGraph = nx.Graph()

		tmpGraph.add_edges_from(elosList)
		tmpGraph = nx.relabel_nodes(tmpGraph, dictNodes)

		# nx.draw(tmpGraph, with_labels=1)
		f = plt.figure(figsize=(10,10))
		f.set_figheight(5)
		f.set_figwidth(10)

		nx.draw_networkx(tmpGraph, with_labels=1,font_size=8)

		file = saveFileIn + "plot-" + list(self.Nodes)[0]
	
		plt.savefig(fname=file, )
g = Grafo()

# g.addElo(Node(0), Node(1))

# g.addElo(Node(1), Node(0))
# g.addElo(Node(1), Node(2))

# g.addElo(Node(2), Node(1))
# g.addElo(Node(2), Node(3))

# g.addElo(Node(3), Node(0))

# g.addElo(Node(9), Node(8))
# g.addElo(Node(8), Node(9))

# g.addElo(Node(0), Node(1))

# g.addElo(Node(1), Node(0))
# g.addElo(Node(1), Node(2))
# g.addElo(Node(1), Node(3))

# g.addElo(Node(2), Node(1))
# g.addElo(Node(2), Node(3))
# g.addElo(Node(2), Node(4))
# g.addElo(Node(2), Node(5))

# g.addElo(Node(3), Node(1))
# g.addElo(Node(3), Node(2))
# g.addElo(Node(3), Node(5))
# g.addElo(Node(3), Node(7))
# g.addElo(Node(3), Node(8))

# g.addElo(Node(4), Node(2))
# g.addElo(Node(4), Node(5))

# g.addElo(Node(5), Node(3))
# g.addElo(Node(5), Node(2))
# g.addElo(Node(5), Node(4))
# g.addElo(Node(5), Node(6))

# g.addElo(Node(6), Node(5))

# g.addElo(Node(7), Node(3))
# g.addElo(Node(7), Node(8))

# g.addElo(Node(8), Node(3))
# g.addElo(Node(8), Node(7))

# g.addElo(Node(9), Node(10))
# g.addElo(Node(10), Node(9))
# g.addElo(Node(10), Node(11))

# g.addElo(Node(11), Node(10))

# g.addElo(Node(15), Node(14))
# g.addElo(Node(15), Node(16))

# g.addElo(Node(0), Node(2))
# # g.addElo(Node(0), Node(1))
# # g.addElo(Node(3), Node(0))

# g.addElo(Node("Bones"), Node("Fullmetal Alchemist: Brotherhood"))
# g.addElo(Node("Bones"), Node("Boku no Hero Academia"))
# g.addElo(Node("Bones"), Node("Noragami"))
# g.addElo(Node("Bones"), Node("Mob Psycho 100"))
# g.addElo(Node("Bones"), Node("Soul Eater"))
# g.addElo(Node("Bones"), Node("Bungou Stray Dogs"))
# g.addElo(Node("Bones"), Node("Darker than Black"))
# g.addElo(Node("Bones"), Node("Kekkai Sensen"))
# g.addElo(Node("Bones"), Node("Carole & Tuesday"))

# g.BFS(7)
# print(g.printGraph())
# g.plotGraph()

# print(g.Nodes[2].Elos)


# g.BFS("MAPPA")
