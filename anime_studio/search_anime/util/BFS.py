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
		return strReturn

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

g = Grafo()

# g.addElo(Node("Bones"), Node("Fullmetal Alchemist: Brotherhood"))
# g.addElo(Node("Bones"), Node("Boku no Hero Academia"))
# g.addElo(Node("Bones"), Node("Noragami"))
# g.addElo(Node("Bones"), Node("Mob Psycho 100"))
# g.addElo(Node("Bones"), Node("Soul Eater"))
# g.addElo(Node("Bones"), Node("Bungou Stray Dogs"))
# g.addElo(Node("Bones"), Node("Darker than Black"))
# g.addElo(Node("Bones"), Node("Kekkai Sensen"))
# g.addElo(Node("Bones"), Node("Carole & Tuesday"))

# g.BFS("Bones")

# g.addElo(Node("Wit Studio"),Node("Shingeki no Kyojin(1 - 3)"))
# g.addElo(Node("Wit Studio"),Node("Owari no Seraph"))
# g.addElo(Node("Wit Studio"),Node("Vinland Saga"))
# g.addElo(Node("Wit Studio"),Node("Koutetsujou no Kabaneri"))
# g.addElo(Node("Wit Studio"),Node("Mahoutsukai no Yome"))
# g.addElo(Node("Wit Studio"),Node("Great Pretender"))
# g.addElo(Node("Wit Studio"),Node("Koi wa Ameagari no You ni"))

# g.BFS("Wit Studio")

# g.addElo(Node("Mappa"), Node("Shingeki no Kyojin(4)"))
# g.addElo(Node("Mappa"), Node("Kakegurui"))
# g.addElo(Node("Mappa"), Node("Zankyou no Terror"))
# g.addElo(Node("Mappa"), Node("Dororo"))
# g.addElo(Node("Mappa"), Node("Jujutsu Kaisen"))
# g.addElo(Node("Mappa"), Node("The God of High School"))
# g.addElo(Node("Mappa"), Node("Inuyashiki"))
# g.addElo(Node("Mappa"), Node("Dorohedoro"))
# g.addElo(Node("Mappa"), Node("Ushio to Tora"))

# g.BFS("Mappa")

# g.addElo(Node("Mad House"), Node("Death Note"))
# g.addElo(Node("Mad House"), Node("One Punch Man"))
# g.addElo(Node("Mad House"), Node("No Game No Life"))
# g.addElo(Node("Mad House"), Node("Hunter x Hunter (2011)"))
# g.addElo(Node("Mad House"), Node("Kiseijuu: Sei no Kakuritsu"))
# g.addElo(Node("Mad House"), Node("Death Parade"))
# g.addElo(Node("Mad House"), Node("Highschool of the Dead"))
# g.addElo(Node("Mad House"), Node("Overlord"))
# g.addElo(Node("Mad House"), Node("Mahouka Koukou no Rettousei"))
# g.addElo(Node("Mad House"), Node("Black Lagoon"))
# g.addElo(Node("Mad House"), Node("Btooom!"))
# g.addElo(Node("Mad House"), Node("Hellsing Ultimate"))
# g.addElo(Node("Mad House"), Node("Monster"))
# g.addElo(Node("Mad House"), Node("Claymore"))
# g.addElo(Node("Mad House"), Node("Ore Monogatari!!"))
# g.addElo(Node("Mad House"), Node("Hajime no Ippo"))
# g.addElo(Node("Mad House"), Node("Paprika"))

# g.BFS("Mad House")

# g.addElo(Node("A-1 Pictures"), Node("Darling in the FranXX"))
# g.addElo(Node("A-1 Pictures"), Node("Sword Art Online"))
# g.addElo(Node("A-1 Pictures"), Node("Shigatsu wa Kimi no Uso"))
# g.addElo(Node("A-1 Pictures"), Node("Ao no Exorcist"))
# g.addElo(Node("A-1 Pictures"), Node("Nanatsu no Taizai"))
# g.addElo(Node("A-1 Pictures"), Node("Boku dake ga Inai Machi"))
# g.addElo(Node("A-1 Pictures"), Node("Fairy Tail"))
# g.addElo(Node("A-1 Pictures"), Node("Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai"))
# g.addElo(Node("A-1 Pictures"), Node("Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen"))
# g.addElo(Node("A-1 Pictures"), Node("Magi: The Labyrinth of Magic"))
# g.addElo(Node("A-1 Pictures"), Node("Gate: Jieitai Kanochi nite, Kaku Tatakaeri"))
# g.addElo(Node("A-1 Pictures"), Node("Hai to Gensou no Grimgar"))
# g.addElo(Node("A-1 Pictures"), Node("Wotaku ni Koi wa Muzukashii"))
# g.addElo(Node("A-1 Pictures"), Node("Gakusen Toshi Asterisk"))
# g.addElo(Node("A-1 Pictures"), Node("Blend S"))
# g.addElo(Node("A-1 Pictures"), Node("Saenai Heroine no Sodatekata"))
# g.addElo(Node("A-1 Pictures"), Node("Aldnoah.Zero"))
# g.addElo(Node("A-1 Pictures"), Node("Ore no Kanojo to Osananajimi ga Shuraba Sugiru"))
# g.addElo(Node("A-1 Pictures"), Node("Ore no Imouto ga Konnani Kawaii Wake ga Nai"))
# g.addElo(Node("A-1 Pictures"), Node("Working!!"))
# g.addElo(Node("A-1 Pictures"), Node("Demi-chan wa Kataritai"))
# g.addElo(Node("A-1 Pictures"), Node("Grancrest Senki"))
            
# g.BFS("A-1 Pictures")

# g.addElo(Node("Ufotable"), Node("Kimetsu no Yaiba"))
# g.addElo(Node("Ufotable"), Node("Fate/Zero"))
# g.addElo(Node("Ufotable"), Node("God Eater"))

# g.BFS("Ufotable")

# g.addElo(Node("JC Staff"), Node("Toradora!"))
# g.addElo(Node("JC Staff"), Node("Shokugeki no Souma"))
# g.addElo(Node("JC Staff"), Node("Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka"))
# g.addElo(Node("JC Staff"), Node("Sakura-sou no Pet na Kanojo"))
# g.addElo(Node("JC Staff"), Node("Kaichou wa Maid-sama!"))
# g.addElo(Node("JC Staff"), Node("Prison School"))
# g.addElo(Node("JC Staff"), Node("Golden Time"))
# g.addElo(Node("JC Staff"), Node("Zero no Tsukaima"))
# g.addElo(Node("JC Staff"), Node("Toaru Majutsu no Index"))
# g.addElo(Node("JC Staff"), Node("Saiki Kusuo no Ψ-nan"))
# g.addElo(Node("JC Staff"), Node("Bakuman"))
# g.addElo(Node("JC Staff"), Node("High Score Girl"))
# g.addElo(Node("JC Staff"), Node("Back Street Girls: Gokudolls"))
            
# g.BFS("JC Staff")

# g.addElo(Node("PA Works"), Node("Angel Beats!"))
# g.addElo(Node("PA Works"), Node("Another"))
# g.addElo(Node("PA Works"), Node("Charlotte"))
# g.addElo(Node("PA Works"), Node("Nagi no Asu kara"))
# g.addElo(Node("PA Works"), Node("Hanasaku Iroha"))
# g.addElo(Node("PA Works"), Node("Kamisama ni Natta Hi"))
            
# g.BFS("PA Works")

# g.addElo(Node("Trigger"), Node("Kill la Kill"))
# g.addElo(Node("Trigger"), Node("Darling in the FranXX"))
# g.addElo(Node("Trigger"), Node("Kiznaiver"))
# g.addElo(Node("Trigger"), Node("Little Witch Academia"))
# g.addElo(Node("Trigger"), Node("SSSS.Gridman"))
# g.addElo(Node("Trigger"), Node("BNA: Brand New Animal"))

# g.BFS("Trigger")

# g.addElo(Node("Kyoto Animation"), Node("Clannad"))
# g.addElo(Node("Kyoto Animation"), Node("Violet Evergarden"))
# g.addElo(Node("Kyoto Animation"), Node("Chuunibyou demo Koi ga Shitai!"))
# g.addElo(Node("Kyoto Animation"), Node("Hyouka"))
# g.addElo(Node("Kyoto Animation"), Node("Kyoukai no Kanata"))
# g.addElo(Node("Kyoto Animation"), Node("K-On!"))
# g.addElo(Node("Kyoto Animation"), Node("Kobayashi-san Chi no Maid Dragon"))
# g.addElo(Node("Kyoto Animation"), Node("Suzumiya Haruhi no Yuuutsu"))
# g.addElo(Node("Kyoto Animation"), Node("Nichijou"))
# g.addElo(Node("Kyoto Animation"), Node("Amagi Brilliant Park"))

# g.BFS("Kyoto Animation")

# g.addElo(Node("Studio Pierrot"), Node("Tokyo Ghoul"))
# g.addElo(Node("Studio Pierrot"), Node("Naruto"))
# g.addElo(Node("Studio Pierrot"), Node("Naruto: Shippuuden"))
# g.addElo(Node("Studio Pierrot"), Node("Bleach"))
# g.addElo(Node("Studio Pierrot"), Node("Black Clover"))
# g.addElo(Node("Studio Pierrot"), Node("Yuu☆Yuu☆Hakusho"))
# g.addElo(Node("Studio Pierrot"), Node("Akudama Drive"))
# g.addElo(Node("Studio Pierrot"), Node("Great Teacher Onizuka"))

# g.BFS("Studio Pierrot")

# g.addElo(Node("White Fox"), Node("Steins;Gate"))
# g.addElo(Node("White Fox"), Node("Re:Zero kara Hajimeru Isekai Seikatsu"))
# g.addElo(Node("White Fox"), Node("Akame ga Kill!"))
# g.addElo(Node("White Fox"), Node("Hataraku Maou-sama!"))
# g.addElo(Node("White Fox"), Node("Goblin Slayer"))
# g.addElo(Node("White Fox"), Node("Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru"))
# g.addElo(Node("White Fox"), Node("Arifureta Shokugyou de Sekai Saikyou"))
            
# g.BFS("White Fox")

# g.addElo(Node("Clover Works"), Node("Yakusoku no Neverland"))
# g.addElo(Node("Clover Works"), Node("Darling in the FranXX"))
# g.addElo(Node("Clover Works"), Node("Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai"))
# g.addElo(Node("Clover Works"), Node("Horimiya"))
# g.addElo(Node("Clover Works"), Node("Wonder Egg Priority"))
# g.addElo(Node("Clover Works"), Node("Persona 5 the Animation"))
            
# g.BFS("Clover Works")

# g.addElo(Node("Toei Animation"), Node("One Piece"))
# g.addElo(Node("Toei Animation"), Node("DragonBall Z"))
# g.addElo(Node("Toei Animation"), Node("Digimon"))
# g.addElo(Node("Toei Animation"), Node("Yu☆Gi☆Oh!"))
            
# g.BFS("Toei Animation")

# g.addElo(Node("Artland"), Node("Mushishi"))

# g.BFS("Artland")

# g.addElo(Node("Kinema Citrus"), Node("Tate no Yuusha no Nariagari"))
# g.addElo(Node("Kinema Citrus"), Node("Made in Abyss"))
# g.addElo(Node("Kinema Citrus"), Node("Black Bullet"))
# g.addElo(Node("Kinema Citrus"), Node("Barakamon"))

# g.BFS("Kinema Citrus")

# g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken"))
# g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken Part 3: Stardust Crusaders"))
# g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken Part 4: Diamond wa Kudakenai"))
# g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken Part 5: Ougon no Kaze"))
# g.addElo(Node("David Production"), Node("Enen no Shouboutai"))
# g.addElo(Node("David Production"), Node("Hataraku Saibou"))

# g.BFS("David Production")

# g.addElo(Node("Studio VOLN"), Node("Ushio to Tora"))
# g.addElo(Node("Studio VOLN"), Node("Karakuri Circus"))

# g.BFS("Studio VOLN")

# g.addElo(Node("Production IG"),Node("Psycho-Pass"))
# g.addElo(Node("Production IG"),Node("Haikyuu!!"))
# g.addElo(Node("Production IG"),Node("Kuroko no Basket"))
# g.addElo(Node("Production IG"),Node("Guilty Crown"))
# g.addElo(Node("Production IG"),Node("Yuukoku no Moriarty"))

# g.BFS("Production IG")

# g.addElo(Node("Gainex"), Node("Tengen Toppa Gurren Lagann"))
# g.addElo(Node("Gainex"), Node("Neon Genesis Evangelion"))

# g.BFS("Gainex")

# g.addElo(Node("TMS Entertainment"), Node("Dr. Stone"))
# g.addElo(Node("TMS Entertainment"), Node("ReLIFE"))
# g.addElo(Node("TMS Entertainment"), Node("D.Gray-man"))
# g.addElo(Node("TMS Entertainment"), Node("Kanojo, Okarishimasu"))
# g.addElo(Node("TMS Entertainment"), Node("Fruits Basket"))
# g.addElo(Node("TMS Entertainment"), Node("Baki"))
# g.addElo(Node("TMS Entertainment"), Node("Zetman"))
# g.addElo(Node("TMS Entertainment"), Node("Saint Seiya: The Lost Canvas - Meiou Shinwa"))
# g.addElo(Node("TMS Entertainment"), Node("Bakugan"))
# g.addElo(Node("TMS Entertainment"), Node("Tottoko Hamtarou"))

# g.BFS("TMS Entertainment")

# g.addElo(Node("feel"), Node("Yahari Ore no Seishun Love Comedy wa Machigatteiru. Zoku"))
# g.addElo(Node("feel"), Node("Tsuki ga Kirei"))
# g.addElo(Node("feel"), Node("Hinamatsuri"))
# g.addElo(Node("feel"), Node("Dagashi Kashi"))
# g.addElo(Node("feel"), Node("Island"))
# g.addElo(Node("feel"), Node("Ushinawareta Mirai wo Motomete"))

# g.BFS("feel")

# g.addElo(Node("Studio Deen"), Node("Kono Subarashii Sekai ni Shukufuku wo!"))
# g.addElo(Node("Studio Deen"), Node("Sakamoto Desu ga?"))
# g.addElo(Node("Studio Deen"), Node("Higurashi no Naku Koro ni"))

# g.BFS("Studio Deen")

g.addElo(Node("Sunrise"), Node("Code Geass"))
g.addElo(Node("Sunrise"), Node("Cowboy Bebop"))
g.addElo(Node("Sunrise"), Node("Gintama"))
g.addElo(Node("Sunrise"), Node("Accel World"))
g.addElo(Node("Sunrise"), Node("Danshi Koukousei no Nichijou"))
g.addElo(Node("Sunrise"), Node("Cross Ange: Tenshi to Ryuu no Rondo"))

g.BFS("Sunrise")

print(g.printLayers())


# print(g.printGraph())
# g.plotGraph()

# print(g.Nodes[2].Elos)


# g.BFS("MAPPA")
