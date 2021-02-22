from collections import defaultdict
import math
import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators.triads import TRIAD_EDGES
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

class Grafo:
	def __init__(self, isDirected: bool = False) -> None:
		self.Nodes = defaultdict(Node)
		self.Elos = []
		self.Name2Int = {}
		self.isDirected = isDirected	
		self.BFSPass = False
		
	def addNode(self, node: Node):

		if type(node.Name) is str and node.Name not in self.Name2Int: # Caso seja uma string salvar um dicionario com numeros correspondentes aos nomes, para o print geral do grafo
			self.Name2Int.update({node.Name: len(self.Nodes)})

		self.Nodes.update({node.Name: node})

	def addElo(self, currentNode: Node, nextNode: Node):
		""" Criação de um elo entre 2 Nodes, os salvando em uma lista de Elos
				e adicionando os novos nodes no dicionario de Nodes existentes.
		"""

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
						adjNode.Visited = True
						adjNode.Layer = currNode.Layer + 1
						queque.append(adjNode)

	def printElos(self, node: str):
		strReturn = ""

		if node in self.Nodes:
			strReturn += f"Estudio {self.Nodes[node].Name}:  "
			nodeList = self.adjNodes(self.Nodes.get(node))
			if nodeList:
				for childNode in nodeList:
					if childNode is nodeList[-1]:
						strReturn += f"{childNode.Name}."
					else:
						strReturn += f"{childNode.Name}, "
		else:
			print("Node não encontrado", end="")
		
		# print(strReturn)
		return strReturn
	
	def printLayers(self):
		strReturn = f"Distancia do node - {list(self.Nodes)[0]}:\n"

		for x in self.Nodes:
			if x != list(self.Nodes)[0]:
				strReturn += f"  {self.Nodes[x].Name}: {self.Nodes[x].Layer}\n"
		return strReturn

	def printVisited(self):
		for i in self.Nodes:
			print(f"{self.Nodes[i].Name}: ")
			for j in self.Nodes[i].Elos:
				print(f"  {self.Nodes[i].Name} - {self.Nodes[i].Elos[j].childNode.Name}: {self.Nodes[i].Elos[j].Visited}")

	def printGraph(self):
		strReturn = ""
		i = 1
		while i < len(self.Nodes):
			strReturn += self.printElos(self.Nodes[list(self.Nodes)[i]].Name)
			strReturn += "\n"
			i += len(self.adjNodes(self.Nodes[list(self.Nodes)[i]]))
		return strReturn

	def printN2S(self):
		"""
		Função para printar uma tabela de auxílio ao plot do grafo geral. 
		"""
		estudios = ["Bones", "Wit Studio", "Mappa", "Mad House", "A-1 Pictures", "Ufotable", "JC Staff", "PA Works", "Trigger", "Kyoto Animation", "Studio Pierrot", "White Fox", "Clover Works", "Toei Animation" ,"Artland", "Kinema Citrus", "David Production", "Studio VOLN", "Production IG", "Gainex", "TMS Entertainment", "feel", "Studio Deen", "Sunrise"]
		print("Start (ID: 0)")
		for n in estudios:
				print(f"Estudio {n} (ID: {self.Name2Int.get(n)}):")
				for i in self.adjNodes(self.Nodes.get(n)):
					if i.Name != "Start":
						print(f"	{i.Name} (ID: {self.Name2Int[i.Name]})")
				print("")
			
				# i+=1

	def plotGraph(self, saveFileIn:str = "./search_anime/util/plot_grafos/", printGeral:bool = False):
		"""
		Função que utiliza dos modulos networkx e matplotlib para poder fazer um plot bonito do grafo, fazemos esse plot
		convertendo o nosso modo de salvar o grafo para um que o networkx consiga utilizar.
		"""
		dictNodes = {}
		elosList = []
		if type(list(self.Nodes)[0]) == int:
			for i in self.Nodes:
				tmp = self.Nodes[i].Name
				dictNodes.update({tmp: tmp})
		else:
			for index, node in enumerate(self.Nodes):
				dictNodes.update({index: self.Nodes[node].Name})
			self.printN2S()
		for elo in self.Elos:
			elosList.append((elo.parentNode.Name, elo.childNode.Name))
		tmpGraph = nx.Graph()

		tmpGraph.add_edges_from(elosList)

		if printGeral:
			tmpGraph = nx.relabel_nodes(tmpGraph, self.Name2Int)

		# nx.draw(tmpGraph, with_labels=1)
		f = plt.figure(figsize=(10,10))
		f.set_figheight(5)
		f.set_figwidth(10)

		nx.draw_networkx(tmpGraph, with_labels=1,font_size=8)

		file = saveFileIn + "plot-" + list(self.Nodes)[0]
	
		#plt.savefig(fname=file, ) # Para salvar o arqv da plot.
		plt.show() # Para mostrar rodando o codigo manualmente.

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

# g.printElos("Bones")
# g.addElo(Node("Wit Studio"),Node("Shingeki no Kyojin(1 - 3)"))
# g.addElo(Node("Wit Studio"),Node("Owari no Seraph"))
# g.addElo(Node("Wit Studio"),Node("Vinland Saga"))
# g.addElo(Node("Wit Studio"),Node("Koutetsujou no Kabaneri"))
# g.addElo(Node("Wit Studio"),Node("Mahoutsukai no Yome"))
# g.addElo(Node("Wit Studio"),Node("Great Pretender"))
# g.addElo(Node("Wit Studio"),Node("Koi wa Ameagari no You ni"))

# g.BFS("Wit Studio")
# g.printElos("Wit Studio")
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
# g.printElos("Mappa")

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
# g.printElos("Mad House")

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
# g.printElos("A-1 Pictures")

# g.addElo(Node("Ufotable"), Node("Kimetsu no Yaiba"))
# g.addElo(Node("Ufotable"), Node("Fate/Zero"))
# g.addElo(Node("Ufotable"), Node("God Eater"))

# g.BFS("Ufotable")
# g.printElos("Ufotable")

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
# g.printElos("JC Staff")

# g.addElo(Node("PA Works"), Node("Angel Beats!"))
# g.addElo(Node("PA Works"), Node("Another"))
# g.addElo(Node("PA Works"), Node("Charlotte"))
# g.addElo(Node("PA Works"), Node("Nagi no Asu kara"))
# g.addElo(Node("PA Works"), Node("Hanasaku Iroha"))
# g.addElo(Node("PA Works"), Node("Kamisama ni Natta Hi"))
# g.BFS("PA Works")
# g.printElos("PA Works")

# g.addElo(Node("Trigger"), Node("Kill la Kill"))
# g.addElo(Node("Trigger"), Node("Darling in the FranXX"))
# g.addElo(Node("Trigger"), Node("Kiznaiver"))
# g.addElo(Node("Trigger"), Node("Little Witch Academia"))
# g.addElo(Node("Trigger"), Node("SSSS.Gridman"))
# g.addElo(Node("Trigger"), Node("BNA: Brand New Animal"))
# g.BFS("Trigger")
# g.printElos("Trigger")

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
# g.printElos("Kyoto Animation")

# g.addElo(Node("Studio Pierrot"), Node("Tokyo Ghoul"))
# g.addElo(Node("Studio Pierrot"), Node("Naruto"))
# g.addElo(Node("Studio Pierrot"), Node("Naruto: Shippuuden"))
# g.addElo(Node("Studio Pierrot"), Node("Bleach"))
# g.addElo(Node("Studio Pierrot"), Node("Black Clover"))
# g.addElo(Node("Studio Pierrot"), Node("Yuu☆Yuu☆Hakusho"))
# g.addElo(Node("Studio Pierrot"), Node("Akudama Drive"))
# g.addElo(Node("Studio Pierrot"), Node("Great Teacher Onizuka"))

# g.BFS("Studio Pierrot")
# g.printElos("Studio Pierrot")

# g.addElo(Node("White Fox"), Node("Steins;Gate"))
# g.addElo(Node("White Fox"), Node("Re:Zero kara Hajimeru Isekai Seikatsu"))
# g.addElo(Node("White Fox"), Node("Akame ga Kill!"))
# g.addElo(Node("White Fox"), Node("Hataraku Maou-sama!"))
# g.addElo(Node("White Fox"), Node("Goblin Slayer"))
# g.addElo(Node("White Fox"), Node("Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru"))
# g.addElo(Node("White Fox"), Node("Arifureta Shokugyou de Sekai Saikyou"))
            
# g.BFS("White Fox")
# g.printElos("White Fox")

# g.addElo(Node("Clover Works"), Node("Yakusoku no Neverland"))
# g.addElo(Node("Clover Works"), Node("Darling in the FranXX"))
# g.addElo(Node("Clover Works"), Node("Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai"))
# g.addElo(Node("Clover Works"), Node("Horimiya"))
# g.addElo(Node("Clover Works"), Node("Wonder Egg Priority"))
# g.addElo(Node("Clover Works"), Node("Persona 5 the Animation"))
            
# g.BFS("Clover Works")
# g.printElos("Clover Works")

# g.addElo(Node("Toei Animation"), Node("One Piece"))
# g.addElo(Node("Toei Animation"), Node("DragonBall Z"))
# g.addElo(Node("Toei Animation"), Node("Digimon"))
# g.addElo(Node("Toei Animation"), Node("Yu☆Gi☆Oh!"))
            
# g.BFS("Toei Animation")
# g.printElos("Toei Animation")

# g.addElo(Node("Artland"), Node("Mushishi"))
# g.BFS("Artland")
# g.printElos("Artland")

# g.addElo(Node("Kinema Citrus"), Node("Tate no Yuusha no Nariagari"))
# g.addElo(Node("Kinema Citrus"), Node("Made in Abyss"))
# g.addElo(Node("Kinema Citrus"), Node("Black Bullet"))
# g.addElo(Node("Kinema Citrus"), Node("Barakamon"))
# g.BFS("Kinema Citrus")
# g.printElos("Kinema Citrus")

# g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken"))
# g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken Part 3: Stardust Crusaders"))
# g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken Part 4: Diamond wa Kudakenai"))
# g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken Part 5: Ougon no Kaze"))
# g.addElo(Node("David Production"), Node("Enen no Shouboutai"))
# g.addElo(Node("David Production"), Node("Hataraku Saibou"))
# g.BFS("David Production")
# g.printElos("David Production")

# g.addElo(Node("Studio VOLN"), Node("Ushio to Tora"))
# g.addElo(Node("Studio VOLN"), Node("Karakuri Circus"))
# g.BFS("Studio VOLN")
# g.printElos("Studio VOLN")

# g.addElo(Node("Production IG"),Node("Psycho-Pass"))
# g.addElo(Node("Production IG"),Node("Haikyuu!!"))
# g.addElo(Node("Production IG"),Node("Kuroko no Basket"))
# g.addElo(Node("Production IG"),Node("Guilty Crown"))
# g.addElo(Node("Production IG"),Node("Yuukoku no Moriarty"))
# g.BFS("Production IG")
# g.printElos("Production IG")

# g.addElo(Node("Gainex"), Node("Tengen Toppa Gurren Lagann"))
# g.addElo(Node("Gainex"), Node("Neon Genesis Evangelion"))
# g.BFS("Gainex")
# g.printElos("Gainex")

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
# g.printElos("TMS Entertainment")

# g.addElo(Node("feel"), Node("Yahari Ore no Seishun Love Comedy wa Machigatteiru. Zoku"))
# g.addElo(Node("feel"), Node("Tsuki ga Kirei"))
# g.addElo(Node("feel"), Node("Hinamatsuri"))
# g.addElo(Node("feel"), Node("Dagashi Kashi"))
# g.addElo(Node("feel"), Node("Island"))
# g.addElo(Node("feel"), Node("Ushinawareta Mirai wo Motomete"))
# g.BFS("feel")
# g.printElos("feel")

# g.addElo(Node("Studio Deen"), Node("Kono Subarashii Sekai ni Shukufuku wo!"))
# g.addElo(Node("Studio Deen"), Node("Sakamoto Desu ga?"))
# g.addElo(Node("Studio Deen"), Node("Higurashi no Naku Koro ni"))
# g.BFS("Studio Deen")
# g.printElos("Studio Deen")

# g.addElo(Node("Sunrise"), Node("Code Geass"))
# g.addElo(Node("Sunrise"), Node("Cowboy Bebop"))
# g.addElo(Node("Sunrise"), Node("Gintama"))
# g.addElo(Node("Sunrise"), Node("Accel World"))
# g.addElo(Node("Sunrise"), Node("Danshi Koukousei no Nichijou"))
# g.addElo(Node("Sunrise"), Node("Cross Ange: Tenshi to Ryuu no Rondo"))
# g.BFS("Sunrise")
# g.printElos("Sunrise")

g.addElo(Node("Start"), Node("Bones"))
g.addElo(Node("Bones"), Node("Fullmetal Alchemist: Brotherhood"))
g.addElo(Node("Bones"), Node("Boku no Hero Academia"))
g.addElo(Node("Bones"), Node("Noragami"))
g.addElo(Node("Bones"), Node("Mob Psycho 100"))
g.addElo(Node("Bones"), Node("Soul Eater"))
g.addElo(Node("Bones"), Node("Bungou Stray Dogs"))
g.addElo(Node("Bones"), Node("Darker than Black"))
g.addElo(Node("Bones"), Node("Kekkai Sensen"))
g.addElo(Node("Bones"), Node("Carole & Tuesday"))

g.addElo(Node("Start"), Node("Wit Studio"))
g.addElo(Node("Wit Studio"), Node("Shingeki no Kyojin(1 - 3)"))
g.addElo(Node("Wit Studio"), Node("Owari no Seraph"))
g.addElo(Node("Wit Studio"), Node("Vinland Saga"))
g.addElo(Node("Wit Studio"), Node("Koutetsujou no Kabaneri"))
g.addElo(Node("Wit Studio"), Node("Mahoutsukai no Yome"))
g.addElo(Node("Wit Studio"), Node("Great Pretender"))
g.addElo(Node("Wit Studio"), Node("Koi wa Ameagari no You ni"))

g.addElo(Node("Start"), Node("Mappa"))
g.addElo(Node("Mappa"), Node("Shingeki no Kyojin(4)"))
g.addElo(Node("Mappa"), Node("Kakegurui"))
g.addElo(Node("Mappa"), Node("Zankyou no Terror"))
g.addElo(Node("Mappa"), Node("Dororo"))
g.addElo(Node("Mappa"), Node("Jujutsu Kaisen"))
g.addElo(Node("Mappa"), Node("The God of High School"))
g.addElo(Node("Mappa"), Node("Inuyashiki"))
g.addElo(Node("Mappa"), Node("Dorohedoro"))
g.addElo(Node("Mappa"), Node("Ushio to Tora"))

g.addElo(Node("Start"), Node("Mad House"))
g.addElo(Node("Mad House"), Node("Death Note"))
g.addElo(Node("Mad House"), Node("One Punch Man"))
g.addElo(Node("Mad House"), Node("No Game No Life"))
g.addElo(Node("Mad House"), Node("Hunter x Hunter (2011)"))
g.addElo(Node("Mad House"), Node("Kiseijuu: Sei no Kakuritsu"))
g.addElo(Node("Mad House"), Node("Death Parade"))
g.addElo(Node("Mad House"), Node("Highschool of the Dead"))
g.addElo(Node("Mad House"), Node("Overlord"))
g.addElo(Node("Mad House"), Node("Mahouka Koukou no Rettousei"))
g.addElo(Node("Mad House"), Node("Black Lagoon"))
g.addElo(Node("Mad House"), Node("Btooom!"))
g.addElo(Node("Mad House"), Node("Hellsing Ultimate"))
g.addElo(Node("Mad House"), Node("Monster"))
g.addElo(Node("Mad House"), Node("Claymore"))
g.addElo(Node("Mad House"), Node("Ore Monogatari!!"))
g.addElo(Node("Mad House"), Node("Hajime no Ippo"))
g.addElo(Node("Mad House"), Node("Paprika"))

g.addElo(Node("Start"), Node("A-1 Pictures"))
g.addElo(Node("A-1 Pictures"), Node("Darling in the FranXX"))
g.addElo(Node("A-1 Pictures"), Node("Sword Art Online"))
g.addElo(Node("A-1 Pictures"), Node("Shigatsu wa Kimi no Uso"))
g.addElo(Node("A-1 Pictures"), Node("Ao no Exorcist"))
g.addElo(Node("A-1 Pictures"), Node("Nanatsu no Taizai"))
g.addElo(Node("A-1 Pictures"), Node("Boku dake ga Inai Machi"))
g.addElo(Node("A-1 Pictures"), Node("Fairy Tail"))
g.addElo(Node("A-1 Pictures"), Node("Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai"))
g.addElo(Node("A-1 Pictures"), Node("Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen"))
g.addElo(Node("A-1 Pictures"), Node("Magi: The Labyrinth of Magic"))
g.addElo(Node("A-1 Pictures"), Node("Gate: Jieitai Kanochi nite, Kaku Tatakaeri"))
g.addElo(Node("A-1 Pictures"), Node("Hai to Gensou no Grimgar"))
g.addElo(Node("A-1 Pictures"), Node("Wotaku ni Koi wa Muzukashii"))
g.addElo(Node("A-1 Pictures"), Node("Gakusen Toshi Asterisk"))
g.addElo(Node("A-1 Pictures"), Node("Blend S"))
g.addElo(Node("A-1 Pictures"), Node("Saenai Heroine no Sodatekata"))
g.addElo(Node("A-1 Pictures"), Node("Aldnoah.Zero"))
g.addElo(Node("A-1 Pictures"), Node("Ore no Kanojo to Osananajimi ga Shuraba Sugiru"))
g.addElo(Node("A-1 Pictures"), Node("Ore no Imouto ga Konnani Kawaii Wake ga Nai"))
g.addElo(Node("A-1 Pictures"), Node("Working!!"))
g.addElo(Node("A-1 Pictures"), Node("Demi-chan wa Kataritai"))
g.addElo(Node("A-1 Pictures"), Node("Grancrest Senki"))

g.addElo(Node("Start"), Node("Ufotable"))
g.addElo(Node("Ufotable"), Node("Kimetsu no Yaiba"))
g.addElo(Node("Ufotable"), Node("Fate/Zero"))
g.addElo(Node("Ufotable"), Node("God Eater"))

g.addElo(Node("Start"), Node("JC Staff"))
g.addElo(Node("JC Staff"), Node("Toradora!"))
g.addElo(Node("JC Staff"), Node("Shokugeki no Souma"))
g.addElo(Node("JC Staff"), Node("Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka"))
g.addElo(Node("JC Staff"), Node("Sakura-sou no Pet na Kanojo"))
g.addElo(Node("JC Staff"), Node("Kaichou wa Maid-sama!"))
g.addElo(Node("JC Staff"), Node("Prison School"))
g.addElo(Node("JC Staff"), Node("Golden Time"))
g.addElo(Node("JC Staff"), Node("Zero no Tsukaima"))
g.addElo(Node("JC Staff"), Node("Toaru Majutsu no Index"))
g.addElo(Node("JC Staff"), Node("Saiki Kusuo no Ψ-nan"))
g.addElo(Node("JC Staff"), Node("Bakuman"))
g.addElo(Node("JC Staff"), Node("High Score Girl"))
g.addElo(Node("JC Staff"), Node("Back Street Girls: Gokudolls"))

g.addElo(Node("Start"), Node("PA Works"))
g.addElo(Node("PA Works"), Node("Angel Beats!"))
g.addElo(Node("PA Works"), Node("Another"))
g.addElo(Node("PA Works"), Node("Charlotte"))
g.addElo(Node("PA Works"), Node("Nagi no Asu kara"))
g.addElo(Node("PA Works"), Node("Hanasaku Iroha"))
g.addElo(Node("PA Works"), Node("Kamisama ni Natta Hi"))

g.addElo(Node("Start"), Node("Trigger"))
g.addElo(Node("Trigger"), Node("Kill la Kill"))
g.addElo(Node("Trigger"), Node("Darling in the FranXX"))
g.addElo(Node("Trigger"), Node("Kiznaiver"))
g.addElo(Node("Trigger"), Node("Little Witch Academia"))
g.addElo(Node("Trigger"), Node("SSSS.Gridman"))
g.addElo(Node("Trigger"), Node("BNA: Brand New Animal"))

g.addElo(Node("Start"), Node("Kyoto Animation"))
g.addElo(Node("Kyoto Animation"), Node("Clannad"))
g.addElo(Node("Kyoto Animation"), Node("Violet Evergarden"))
g.addElo(Node("Kyoto Animation"), Node("Chuunibyou demo Koi ga Shitai!"))
g.addElo(Node("Kyoto Animation"), Node("Hyouka"))
g.addElo(Node("Kyoto Animation"), Node("Kyoukai no Kanata"))
g.addElo(Node("Kyoto Animation"), Node("K-On!"))
g.addElo(Node("Kyoto Animation"), Node("Kobayashi-san Chi no Maid Dragon"))
g.addElo(Node("Kyoto Animation"), Node("Suzumiya Haruhi no Yuuutsu"))
g.addElo(Node("Kyoto Animation"), Node("Nichijou"))
g.addElo(Node("Kyoto Animation"), Node("Amagi Brilliant Park"))

g.addElo(Node("Start"), Node("Studio Pierrot"))
g.addElo(Node("Studio Pierrot"), Node("Tokyo Ghoul"))
g.addElo(Node("Studio Pierrot"), Node("Naruto"))
g.addElo(Node("Studio Pierrot"), Node("Naruto: Shippuuden"))
g.addElo(Node("Studio Pierrot"), Node("Bleach"))
g.addElo(Node("Studio Pierrot"), Node("Black Clover"))
g.addElo(Node("Studio Pierrot"), Node("Yuu☆Yuu☆Hakusho"))
g.addElo(Node("Studio Pierrot"), Node("Akudama Drive"))
g.addElo(Node("Studio Pierrot"), Node("Great Teacher Onizuka"))

g.addElo(Node("Start"), Node("White Fox"))
g.addElo(Node("White Fox"), Node("Steins;Gate"))
g.addElo(Node("White Fox"), Node("Re:Zero kara Hajimeru Isekai Seikatsu"))
g.addElo(Node("White Fox"), Node("Akame ga Kill!"))
g.addElo(Node("White Fox"), Node("Hataraku Maou-sama!"))
g.addElo(Node("White Fox"), Node("Goblin Slayer"))
g.addElo(Node("White Fox"), Node("Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru"))
g.addElo(Node("White Fox"), Node("Arifureta Shokugyou de Sekai Saikyou"))

g.addElo(Node("Start"), Node("Clover Works"))
g.addElo(Node("Clover Works"), Node("Yakusoku no Neverland"))
g.addElo(Node("Clover Works"), Node("Darling in the FranXX"))
g.addElo(Node("Clover Works"), Node("Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai"))
g.addElo(Node("Clover Works"), Node("Horimiya"))
g.addElo(Node("Clover Works"), Node("Wonder Egg Priority"))
g.addElo(Node("Clover Works"), Node("Persona 5 the Animation"))

g.addElo(Node("Start"), Node("Toei Animation"))
g.addElo(Node("Toei Animation"), Node("One Piece"))
g.addElo(Node("Toei Animation"), Node("DragonBall Z"))
g.addElo(Node("Toei Animation"), Node("Digimon"))
g.addElo(Node("Toei Animation"), Node("Yu☆Gi☆Oh!"))

g.addElo(Node("Start"), Node("Artland"))
g.addElo(Node("Artland"), Node("Mushishi"))

g.addElo(Node("Start"), Node("Kinema Citrus"))
g.addElo(Node("Kinema Citrus"), Node("Tate no Yuusha no Nariagari"))
g.addElo(Node("Kinema Citrus"), Node("Made in Abyss"))
g.addElo(Node("Kinema Citrus"), Node("Black Bullet"))
g.addElo(Node("Kinema Citrus"), Node("Barakamon"))

g.addElo(Node("Start"), Node("David Production"))
g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken"))
g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken Part 3: Stardust Crusaders"))
g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken Part 4: Diamond wa Kudakenai"))
g.addElo(Node("David Production"), Node("JoJo no Kimyou na Bouken Part 5: Ougon no Kaze"))
g.addElo(Node("David Production"), Node("Enen no Shouboutai"))
g.addElo(Node("David Production"), Node("Hataraku Saibou"))

g.addElo(Node("Start"), Node("Studio VOLN"))
g.addElo(Node("Studio VOLN"), Node("Ushio to Tora"))
g.addElo(Node("Studio VOLN"), Node("Karakuri Circus"))

g.addElo(Node("Start"), Node("Production IG"))
g.addElo(Node("Production IG"), Node("Psycho-Pass"))
g.addElo(Node("Production IG"), Node("Haikyuu!!"))
g.addElo(Node("Production IG"), Node("Kuroko no Basket"))
g.addElo(Node("Production IG"), Node("Guilty Crown"))
g.addElo(Node("Production IG"), Node("Yuukoku no Moriarty"))

g.addElo(Node("Start"), Node("Gainex"))
g.addElo(Node("Gainex"), Node("Tengen Toppa Gurren Lagann"))
g.addElo(Node("Gainex"), Node("Neon Genesis Evangelion"))

g.addElo(Node("Start"), Node("TMS Entertainment"))
g.addElo(Node("TMS Entertainment"), Node("Dr. Stone"))
g.addElo(Node("TMS Entertainment"), Node("ReLIFE"))
g.addElo(Node("TMS Entertainment"), Node("D.Gray-man"))
g.addElo(Node("TMS Entertainment"), Node("Kanojo, Okarishimasu"))
g.addElo(Node("TMS Entertainment"), Node("Fruits Basket"))
g.addElo(Node("TMS Entertainment"), Node("Baki"))
g.addElo(Node("TMS Entertainment"), Node("Zetman"))
g.addElo(Node("TMS Entertainment"), Node("Saint Seiya: The Lost Canvas - Meiou Shinwa"))
g.addElo(Node("TMS Entertainment"), Node("Bakugan"))
g.addElo(Node("TMS Entertainment"), Node("Tottoko Hamtarou"))

g.addElo(Node("Start"), Node("feel"))
g.addElo(Node("feel"), Node("Yahari Ore no Seishun Love Comedy wa Machigatteiru. Zoku"))
g.addElo(Node("feel"), Node("Tsuki ga Kirei"))
g.addElo(Node("feel"), Node("Hinamatsuri"))
g.addElo(Node("feel"), Node("Dagashi Kashi"))
g.addElo(Node("feel"), Node("Island"))
g.addElo(Node("feel"), Node("Ushinawareta Mirai wo Motomete"))

g.addElo(Node("Start"), Node("Studio Deen"))
g.addElo(Node("Studio Deen"), Node("Kono Subarashii Sekai ni Shukufuku wo!"))
g.addElo(Node("Studio Deen"), Node("Sakamoto Desu ga?"))
g.addElo(Node("Studio Deen"), Node("Higurashi no Naku Koro ni"))

g.addElo(Node("Start"), Node("Sunrise"))
g.addElo(Node("Sunrise"), Node("Code Geass"))
g.addElo(Node("Sunrise"), Node("Cowboy Bebop"))
g.addElo(Node("Sunrise"), Node("Gintama"))
g.addElo(Node("Sunrise"), Node("Accel World"))
g.addElo(Node("Sunrise"), Node("Danshi Koukousei no Nichijou"))
g.addElo(Node("Sunrise"), Node("Cross Ange: Tenshi to Ryuu no Rondo"))

g.BFS("Start")
# print(g.printLayers())
g.plotGraph(saveFileIn="./PA/Grafos1_PauloGoncalves_PedroVitor/anime_studio/search_anime/util/plot_grafos/", printGeral=True)


