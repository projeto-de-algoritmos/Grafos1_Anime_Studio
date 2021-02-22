from django.shortcuts import render
from django.http import HttpResponse
from search_anime.util import Graph

def helloWorld(request):
    return HttpResponse('Hello World')

def home(request):
    return render(request, 'search_anime/home.html')

def bones(request):
    return render(request, 'search_anime/bones.html')

def wit(request):
    return render(request, 'search_anime/wit.html')

def mappa(request):
    return render(request, 'search_anime/mappa.html')

def madhouse(request):
    return render(request, 'search_anime/madhouse.html')

def apic(request):
    return render(request, 'search_anime/apic.html')

def ufotable(request):
    return render(request, 'search_anime/ufotable.html')

def jcstaff(request):
    return render(request, 'search_anime/jcstaff.html')

def paworks(request):
    return render(request, 'search_anime/paworks.html')

def trigger(request):
    return render(request, 'search_anime/trigger.html')

def kyoto(request):
    return render(request, 'search_anime/kyoto.html')

def pierrot(request):
    return render(request, 'search_anime/pierrot.html')

def whitefox(request):
    return render(request, 'search_anime/whitefox.html')

def clover(request):
    return render(request, 'search_anime/clover.html')

def toei(request):
    return render(request, 'search_anime/toei.html')

def artland(request):
    return render(request, 'search_anime/artland.html')

def kinema(request):
    return render(request, 'search_anime/kinema.html')

def david(request):
    return render(request, 'search_anime/david.html')

def voln(request):
    return render(request, 'search_anime/voln.html')

def ig(request):
    return render(request, 'search_anime/ig.html')

def gainax(request):
    return render(request, 'search_anime/gainax.html')

def tms(request):
    return render(request, 'search_anime/tms.html')

def feel(request):
    return render(request, 'search_anime/feel.html')

def deen(request):
    return render(request, 'search_anime/deen.html')

def sunrise(request):
    return render(request, 'search_anime/sunrise.html')

def geral(request):
    return render(request, 'search_anime/geral.html')

def projeto(request):
    g = Graph.Grafo()


    template = 'search_anime/projeto.html'
    context = {}
    if request.method == 'POST':
        if request.POST.get("bones"):
            g.addElo(Graph.Node("Bones"), Graph.Node("Fullmetal Alchemist: Brotherhood"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Boku no Hero Academia"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Noragami"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Mob Psycho 100"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Soul Eater"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Bungou Stray Dogs"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Darker than Black"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Kekkai Sensen"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Carole & Tuesday"))

            g.BFS("Bones")
            g.plotGraph()
            # g.printLayers()

            context =  {
                'nosso_grafo': g.printElos("Bones"),
                'distancia_grafo': g.printLayers(),
            }


            template = 'search_anime/bones.html'

        elif request.POST.get("wit"):
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Shingeki no Kyojin(1 - 3)"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Owari no Seraph"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Vinland Saga"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Koutetsujou no Kabaneri"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Mahoutsukai no Yome"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Great Pretender"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Koi wa Ameagari no You ni"))

            g.BFS("Wit Studio")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Wit Studio"),
            }
            
            template = 'search_anime/wit.html'

        elif request.POST.get("mappa"):
            g.addElo(Graph.Node("Mappa"), Graph.Node("Shingeki no Kyojin(4)"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Kakegurui"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Zankyou no Terror"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Dororo"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Jujutsu Kaisen"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("The God of High School"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Inuyashiki"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Dorohedoro"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Ushio to Tora"))

            g.BFS("Mappa")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Mappa"),
            }
            template = 'search_anime/mappa.html'

        elif request.POST.get("madhouse"):
            g.addElo(Graph.Node("Mad House"), Graph.Node("Death Note"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("One Punch Man"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("No Game No Life"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Hunter x Hunter (2011)"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Kiseijuu: Sei no Kakuritsu"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Death Parade"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Highschool of the Dead"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Overlord"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Mahouka Koukou no Rettousei"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Black Lagoon"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Btooom!"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Hellsing Ultimate"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Monster"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Claymore"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Ore Monogatari!!"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Hajime no Ippo"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Paprika"))

            g.BFS("Mad House")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Mad House"),
            }
            template = 'search_anime/madhouse.html'

        elif request.POST.get("a1"):
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Darling in the FranXX"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Sword Art Online"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Shigatsu wa Kimi no Uso"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Ao no Exorcist"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Nanatsu no Taizai"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Boku dake ga Inai Machi"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Fairy Tail"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Magi: The Labyrinth of Magic"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Gate: Jieitai Kanochi nite, Kaku Tatakaeri"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Hai to Gensou no Grimgar"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Wotaku ni Koi wa Muzukashii"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Gakusen Toshi Asterisk"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Blend S"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Saenai Heroine no Sodatekata"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Aldnoah.Zero"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Ore no Kanojo to Osananajimi ga Shuraba Sugiru"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Ore no Imouto ga Konnani Kawaii Wake ga Nai"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Working!!"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Demi-chan wa Kataritai"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Grancrest Senki"))
            
            g.BFS("A-1 Pictures")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("A-1 Pictures"),
            }
            template = 'search_anime/apic.html'

        elif request.POST.get("ufotable"):
            g.addElo(Graph.Node("Ufotable"), Graph.Node("Kimetsu no Yaiba"))
            g.addElo(Graph.Node("Ufotable"), Graph.Node("Fate/Zero"))
            g.addElo(Graph.Node("Ufotable"), Graph.Node("God Eater"))

            g.BFS("Ufotable")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos(""),
            }
            template = 'search_anime/ufotable.html'

        elif request.POST.get("jcstaff"):
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Toradora!"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Shokugeki no Souma"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Sakura-sou no Pet na Kanojo"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Kaichou wa Maid-sama!"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Prison School"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Golden Time"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Zero no Tsukaima"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Toaru Majutsu no Index"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Saiki Kusuo no Ψ-nan"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Bakuman"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("High Score Girl"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Back Street Girls: Gokudolls"))
            
            g.BFS("JC Staff")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("JC Staff"),
            }
            template = 'search_anime/jcstaff.html'

        elif request.POST.get("paworks"):
            g.addElo(Graph.Node("PA Works"), Graph.Node("Angel Beats!"))
            g.addElo(Graph.Node("PA Works"), Graph.Node("Another"))
            g.addElo(Graph.Node("PA Works"), Graph.Node("Charlotte"))
            g.addElo(Graph.Node("PA Works"), Graph.Node("Nagi no Asu kara"))
            g.addElo(Graph.Node("PA Works"), Graph.Node("Hanasaku Iroha"))
            g.addElo(Graph.Node("PA Works"), Graph.Node("Kamisama ni Natta Hi"))
            
            g.BFS("PA Works")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("PA Works"),
            }
            template = 'search_anime/paworks.html'

        elif request.POST.get("trigger"):
            g.addElo(Graph.Node("Trigger"), Graph.Node("Kill la Kill"))
            g.addElo(Graph.Node("Trigger"), Graph.Node("Darling in the FranXX"))
            g.addElo(Graph.Node("Trigger"), Graph.Node("Kiznaiver"))
            g.addElo(Graph.Node("Trigger"), Graph.Node("Little Witch Academia"))
            g.addElo(Graph.Node("Trigger"), Graph.Node("SSSS.Gridman"))
            g.addElo(Graph.Node("Trigger"), Graph.Node("BNA: Brand New Animal"))

            g.BFS("Trigger")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Trigger"),
            }
            template = 'search_anime/trigger.html'

        elif request.POST.get("kyoto"):
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Clannad"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Violet Evergarden"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Chuunibyou demo Koi ga Shitai!"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Hyouka"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Kyoukai no Kanata"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("K-On!"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Kobayashi-san Chi no Maid Dragon"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Suzumiya Haruhi no Yuuutsu"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Nichijou"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Amagi Brilliant Park"))

            g.BFS("Kyoto Animation")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Kyoto Animation"),
            }
            template = 'search_anime/kyoto.html'

        elif request.POST.get("pierrot"):
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Tokyo Ghoul"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Naruto"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Naruto: Shippuuden"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Bleach"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Black Clover"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Yuu☆Yuu☆Hakusho"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Akudama Drive"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Great Teacher Onizuka"))

            g.BFS("Studio Pierrot")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Studio Pierrot"),
            }
            template = 'search_anime/pierrot.html'

        elif request.POST.get("fox"):
            g.addElo(Graph.Node("White Fox"), Graph.Node("Steins;Gate"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Re:Zero kara Hajimeru Isekai Seikatsu"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Akame ga Kill!"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Hataraku Maou-sama!"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Goblin Slayer"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Arifureta Shokugyou de Sekai Saikyou"))
            
            g.BFS("White Fox")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("White Fox"),
            }
            template = 'search_anime/whitefox.html'

        elif request.POST.get("clover"):
            g.addElo(Graph.Node("Clover Works"), Graph.Node("Yakusoku no Neverland"))
            g.addElo(Graph.Node("Clover Works"), Graph.Node("Darling in the FranXX"))
            g.addElo(Graph.Node("Clover Works"), Graph.Node("Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai"))
            g.addElo(Graph.Node("Clover Works"), Graph.Node("Horimiya"))
            g.addElo(Graph.Node("Clover Works"), Graph.Node("Wonder Egg Priority"))
            g.addElo(Graph.Node("Clover Works"), Graph.Node("Persona 5 the Animation"))
            
            g.BFS("Clover Works")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Clover Works"),
            }
            template = 'search_anime/clover.html'

        elif request.POST.get("toei"):
            g.addElo(Graph.Node("Toei Animation"), Graph.Node("One Piece"))
            g.addElo(Graph.Node("Toei Animation"), Graph.Node("DragonBall Z"))
            g.addElo(Graph.Node("Toei Animation"), Graph.Node("Digimon"))
            g.addElo(Graph.Node("Toei Animation"), Graph.Node("Yu☆Gi☆Oh!"))
            
            g.BFS("Toei Animation")
            g.plotGraph()
            
            context =  {
                'nosso_grafo': g.printElos("Toei Animation"),
            }
            template = 'search_anime/toei.html'

        elif request.POST.get("artland"):
            g.addElo(Graph.Node("Artland"), Graph.Node("Mushishi"))

            g.BFS("Artland")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Artland"),
            }
            template = 'search_anime/artland.html'

        elif request.POST.get("kinema"):
            g.addElo(Graph.Node("Kinema Citrus"), Graph.Node("Tate no Yuusha no Nariagari"))
            g.addElo(Graph.Node("Kinema Citrus"), Graph.Node("Made in Abyss"))
            g.addElo(Graph.Node("Kinema Citrus"), Graph.Node("Black Bullet"))
            g.addElo(Graph.Node("Kinema Citrus"), Graph.Node("Barakamon"))

            g.BFS("Kinema Citrus")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Kinema Citrus"),
            }
            template = 'search_anime/kinema.html'
        elif request.POST.get("david"):
            g.addElo(Graph.Node("David Production"), Graph.Node("JoJo no Kimyou na Bouken"))
            g.addElo(Graph.Node("David Production"), Graph.Node("JoJo no Kimyou na Bouken Part 3: Stardust Crusaders"))
            g.addElo(Graph.Node("David Production"), Graph.Node("JoJo no Kimyou na Bouken Part 4: Diamond wa Kudakenai"))
            g.addElo(Graph.Node("David Production"), Graph.Node("JoJo no Kimyou na Bouken Part 5: Ougon no Kaze"))
            g.addElo(Graph.Node("David Production"), Graph.Node("Enen no Shouboutai"))
            g.addElo(Graph.Node("David Production"), Graph.Node("Hataraku Saibou"))

            g.BFS("David Production")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("David Production"),
            }
            template = 'search_anime/david.html'

        elif request.POST.get("voln"):
            g.addElo(Graph.Node("Studio VOLN"), Graph.Node("Ushio to Tora"))
            g.addElo(Graph.Node("Studio VOLN"), Graph.Node("Karakuri Circus"))

            g.BFS("Studio VOLN")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Studio VOLN"),
            }
            template = 'search_anime/voln.html'

        elif request.POST.get("ig"):
            g.addElo(Graph.Node("Production IG"), Graph.Node("Psycho-Pass"))
            g.addElo(Graph.Node("Production IG"), Graph.Node("Haikyuu!!"))
            g.addElo(Graph.Node("Production IG"), Graph.Node("Kuroko no Basket"))
            g.addElo(Graph.Node("Production IG"), Graph.Node("Guilty Crown"))
            g.addElo(Graph.Node("Production IG"), Graph.Node("Yuukoku no Moriarty"))

            g.BFS("Production IG")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Production IG"),
            }
            template = 'search_anime/ig.html'

        elif request.POST.get("gainex"):
            g.addElo(Graph.Node("Gainex"), Graph.Node("Tengen Toppa Gurren Lagann"))
            g.addElo(Graph.Node("Gainex"), Graph.Node("Neon Genesis Evangelion"))

            g.BFS("Gainex")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Gainex"),
            }
            template = 'search_anime/gainax.html'

        elif request.POST.get("tms"):
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Dr. Stone"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("ReLIFE"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("D.Gray-man"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Kanojo, Okarishimasu"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Fruits Basket"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Baki"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Zetman"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Saint Seiya: The Lost Canvas - Meiou Shinwa"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Bakugan"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Tottoko Hamtarou"))

            g.BFS("TMS Entertainment")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("TMS Entertainment"),
            }
            template = 'search_anime/tms.html'

        elif request.POST.get("feel"):
            g.addElo(Graph.Node("feel"), Graph.Node("Yahari Ore no Seishun Love Comedy wa Machigatteiru. Zoku"))
            g.addElo(Graph.Node("feel"), Graph.Node("Tsuki ga Kirei"))
            g.addElo(Graph.Node("feel"), Graph.Node("Hinamatsuri"))
            g.addElo(Graph.Node("feel"), Graph.Node("Dagashi Kashi"))
            g.addElo(Graph.Node("feel"), Graph.Node("Island"))
            g.addElo(Graph.Node("feel"), Graph.Node("Ushinawareta Mirai wo Motomete"))

            g.BFS("feel")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("feel"),
            }
            template = 'search_anime/feel.html'

        elif request.POST.get("deen"):
            g.addElo(Graph.Node("Studio Deen"), Graph.Node("Kono Subarashii Sekai ni Shukufuku wo!"))
            g.addElo(Graph.Node("Studio Deen"), Graph.Node("Sakamoto Desu ga?"))
            g.addElo(Graph.Node("Studio Deen"), Graph.Node("Higurashi no Naku Koro ni"))

            g.BFS("Studio Deen")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Studio Deen"),
            }
            template = 'search_anime/deen.html'

        elif request.POST.get("sunrise"):
            g.addElo(Graph.Node("Sunrise"), Graph.Node("Code Geass"))
            g.addElo(Graph.Node("Sunrise"), Graph.Node("Cowboy Bebop"))
            g.addElo(Graph.Node("Sunrise"), Graph.Node("Gintama"))
            g.addElo(Graph.Node("Sunrise"), Graph.Node("Accel World"))
            g.addElo(Graph.Node("Sunrise"), Graph.Node("Danshi Koukousei no Nichijou"))
            g.addElo(Graph.Node("Sunrise"), Graph.Node("Cross Ange: Tenshi to Ryuu no Rondo"))

            g.BFS("Sunrise")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Sunrise"),
            }
            template = 'search_anime/sunrise.html'

        elif request.POST.get("geral"):
            g.addElo(Graph.Node("Start"), Graph.Node("A1 Pictures"))
            g.addElo(Graph.Node("Start"), Graph.Node("Artland"))
            g.addElo(Graph.Node("Start"), Graph.Node("Bones"))
            g.addElo(Graph.Node("Start"), Graph.Node("Clover Works"))
            g.addElo(Graph.Node("Start"), Graph.Node("David Production"))
            g.addElo(Graph.Node("Start"), Graph.Node("Studio Deen"))
            g.addElo(Graph.Node("Start"), Graph.Node("feel"))
            g.addElo(Graph.Node("Start"), Graph.Node("Gainax"))
            g.addElo(Graph.Node("Start"), Graph.Node("Production IG"))
            g.addElo(Graph.Node("Start"), Graph.Node("JC Staff"))
            g.addElo(Graph.Node("Start"), Graph.Node("Kinema Citrus"))
            g.addElo(Graph.Node("Start"), Graph.Node("Kyoto Animation"))
            g.addElo(Graph.Node("Start"), Graph.Node("Mad House"))
            g.addElo(Graph.Node("Start"), Graph.Node("Mappa"))
            g.addElo(Graph.Node("Start"), Graph.Node("PA Works"))
            g.addElo(Graph.Node("Start"), Graph.Node("Studio Pierrot"))
            g.addElo(Graph.Node("Start"), Graph.Node("Sunrise"))
            g.addElo(Graph.Node("Start"), Graph.Node("TMS Entertainment"))
            g.addElo(Graph.Node("Start"), Graph.Node("Toei Animation"))
            g.addElo(Graph.Node("Start"), Graph.Node("Trigger"))
            g.addElo(Graph.Node("Start"), Graph.Node("Ufotable"))
            g.addElo(Graph.Node("Start"), Graph.Node("Studio VOLN"))
            g.addElo(Graph.Node("Start"), Graph.Node("White Fox"))
            g.addElo(Graph.Node("Start"), Graph.Node("Wit Studio"))

            g.addElo(Graph.Node("Bones"), Graph.Node("Fullmetal Alchemist: Brotherhood"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Boku no Hero Academia"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Noragami"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Mob Psycho 100"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Soul Eater"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Bungou Stray Dogs"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Darker than Black"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Kekkai Sensen"))
            g.addElo(Graph.Node("Bones"), Graph.Node("Carole & Tuesday"))

            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Shingeki no Kyojin(1 - 3)"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Owari no Seraph"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Vinland Saga"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Koutetsujou no Kabaneri"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Mahoutsukai no Yome"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Great Pretender"))
            g.addElo(Graph.Node("Wit Studio"), Graph.Node("Koi wa Ameagari no You ni"))

            g.addElo(Graph.Node("Mappa"), Graph.Node("Shingeki no Kyojin(4)"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Kakegurui"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Zankyou no Terror"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Dororo"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Jujutsu Kaisen"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("The God of High School"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Inuyashiki"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Dorohedoro"))
            g.addElo(Graph.Node("Mappa"), Graph.Node("Ushio to Tora"))

            g.addElo(Graph.Node("Mad House"), Graph.Node("Death Note"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("One Punch Man"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("No Game No Life"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Hunter x Hunter (2011)"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Kiseijuu: Sei no Kakuritsu"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Death Parade"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Highschool of the Dead"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Overlord"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Mahouka Koukou no Rettousei"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Black Lagoon"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Btooom!"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Hellsing Ultimate"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Monster"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Claymore"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Ore Monogatari!!"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Hajime no Ippo"))
            g.addElo(Graph.Node("Mad House"), Graph.Node("Paprika"))

            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Darling in the FranXX"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Sword Art Online"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Shigatsu wa Kimi no Uso"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Ao no Exorcist"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Nanatsu no Taizai"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Boku dake ga Inai Machi"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Fairy Tail"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Magi: The Labyrinth of Magic"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Gate: Jieitai Kanochi nite, Kaku Tatakaeri"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Hai to Gensou no Grimgar"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Wotaku ni Koi wa Muzukashii"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Gakusen Toshi Asterisk"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Blend S"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Saenai Heroine no Sodatekata"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Aldnoah.Zero"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Ore no Kanojo to Osananajimi ga Shuraba Sugiru"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Ore no Imouto ga Konnani Kawaii Wake ga Nai"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Working!!"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Demi-chan wa Kataritai"))
            g.addElo(Graph.Node("A-1 Pictures"), Graph.Node("Grancrest Senki"))

            g.addElo(Graph.Node("Ufotable"), Graph.Node("Kimetsu no Yaiba"))
            g.addElo(Graph.Node("Ufotable"), Graph.Node("Fate/Zero"))
            g.addElo(Graph.Node("Ufotable"), Graph.Node("God Eater"))

            g.addElo(Graph.Node("JC Staff"), Graph.Node("Toradora!"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Shokugeki no Souma"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Sakura-sou no Pet na Kanojo"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Kaichou wa Maid-sama!"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Prison School"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Golden Time"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Zero no Tsukaima"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Toaru Majutsu no Index"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Saiki Kusuo no Ψ-nan"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Bakuman"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("High Score Girl"))
            g.addElo(Graph.Node("JC Staff"), Graph.Node("Back Street Girls: Gokudolls"))

            g.addElo(Graph.Node("PA Works"), Graph.Node("Angel Beats!"))
            g.addElo(Graph.Node("PA Works"), Graph.Node("Another"))
            g.addElo(Graph.Node("PA Works"), Graph.Node("Charlotte"))
            g.addElo(Graph.Node("PA Works"), Graph.Node("Nagi no Asu kara"))
            g.addElo(Graph.Node("PA Works"), Graph.Node("Hanasaku Iroha"))
            g.addElo(Graph.Node("PA Works"), Graph.Node("Kamisama ni Natta Hi"))

            g.addElo(Graph.Node("Trigger"), Graph.Node("Kill la Kill"))
            g.addElo(Graph.Node("Trigger"), Graph.Node("Darling in the FranXX"))
            g.addElo(Graph.Node("Trigger"), Graph.Node("Kiznaiver"))
            g.addElo(Graph.Node("Trigger"), Graph.Node("Little Witch Academia"))
            g.addElo(Graph.Node("Trigger"), Graph.Node("SSSS.Gridman"))
            g.addElo(Graph.Node("Trigger"), Graph.Node("BNA: Brand New Animal"))

            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Clannad"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Violet Evergarden"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Chuunibyou demo Koi ga Shitai!"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Hyouka"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Kyoukai no Kanata"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("K-On!"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Kobayashi-san Chi no Maid Dragon"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Suzumiya Haruhi no Yuuutsu"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Nichijou"))
            g.addElo(Graph.Node("Kyoto Animation"), Graph.Node("Amagi Brilliant Park"))

            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Tokyo Ghoul"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Naruto"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Naruto: Shippuuden"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Bleach"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Black Clover"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Yuu☆Yuu☆Hakusho"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Akudama Drive"))
            g.addElo(Graph.Node("Studio Pierrot"), Graph.Node("Great Teacher Onizuka"))

            g.addElo(Graph.Node("White Fox"), Graph.Node("Steins;Gate"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Re:Zero kara Hajimeru Isekai Seikatsu"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Akame ga Kill!"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Hataraku Maou-sama!"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Goblin Slayer"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru"))
            g.addElo(Graph.Node("White Fox"), Graph.Node("Arifureta Shokugyou de Sekai Saikyou"))

            g.addElo(Graph.Node("Clover Works"), Graph.Node("Yakusoku no Neverland"))
            g.addElo(Graph.Node("Clover Works"), Graph.Node("Darling in the FranXX"))
            g.addElo(Graph.Node("Clover Works"), Graph.Node("Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai"))
            g.addElo(Graph.Node("Clover Works"), Graph.Node("Horimiya"))
            g.addElo(Graph.Node("Clover Works"), Graph.Node("Wonder Egg Priority"))
            g.addElo(Graph.Node("Clover Works"), Graph.Node("Persona 5 the Animation"))

            g.addElo(Graph.Node("Toei Animation"), Graph.Node("One Piece"))
            g.addElo(Graph.Node("Toei Animation"), Graph.Node("DragonBall Z"))
            g.addElo(Graph.Node("Toei Animation"), Graph.Node("Digimon"))
            g.addElo(Graph.Node("Toei Animation"), Graph.Node("Yu☆Gi☆Oh!"))

            g.addElo(Graph.Node("Artland"), Graph.Node("Mushishi"))

            g.addElo(Graph.Node("Kinema Citrus"), Graph.Node("Tate no Yuusha no Nariagari"))
            g.addElo(Graph.Node("Kinema Citrus"), Graph.Node("Made in Abyss"))
            g.addElo(Graph.Node("Kinema Citrus"), Graph.Node("Black Bullet"))
            g.addElo(Graph.Node("Kinema Citrus"), Graph.Node("Barakamon"))

            g.addElo(Graph.Node("David Production"), Graph.Node("JoJo no Kimyou na Bouken"))
            g.addElo(Graph.Node("David Production"), Graph.Node("JoJo no Kimyou na Bouken Part 3: Stardust Crusaders"))
            g.addElo(Graph.Node("David Production"), Graph.Node("JoJo no Kimyou na Bouken Part 4: Diamond wa Kudakenai"))
            g.addElo(Graph.Node("David Production"), Graph.Node("JoJo no Kimyou na Bouken Part 5: Ougon no Kaze"))
            g.addElo(Graph.Node("David Production"), Graph.Node("Enen no Shouboutai"))
            g.addElo(Graph.Node("David Production"), Graph.Node("Hataraku Saibou"))

            g.addElo(Graph.Node("Studio VOLN"), Graph.Node("Ushio to Tora"))
            g.addElo(Graph.Node("Studio VOLN"), Graph.Node("Karakuri Circus"))

            g.addElo(Graph.Node("Production IG"), Graph.Node("Psycho-Pass"))
            g.addElo(Graph.Node("Production IG"), Graph.Node("Haikyuu!!"))
            g.addElo(Graph.Node("Production IG"), Graph.Node("Kuroko no Basket"))
            g.addElo(Graph.Node("Production IG"), Graph.Node("Guilty Crown"))
            g.addElo(Graph.Node("Production IG"), Graph.Node("Yuukoku no Moriarty"))

            g.addElo(Graph.Node("Gainex"), Graph.Node("Tengen Toppa Gurren Lagann"))
            g.addElo(Graph.Node("Gainex"), Graph.Node("Neon Genesis Evangelion"))

            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Dr. Stone"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("ReLIFE"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("D.Gray-man"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Kanojo, Okarishimasu"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Fruits Basket"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Baki"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Zetman"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Saint Seiya: The Lost Canvas - Meiou Shinwa"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Bakugan"))
            g.addElo(Graph.Node("TMS Entertainment"), Graph.Node("Tottoko Hamtarou"))

            g.addElo(Graph.Node("feel"), Graph.Node("Yahari Ore no Seishun Love Comedy wa Machigatteiru. Zoku"))
            g.addElo(Graph.Node("feel"), Graph.Node("Tsuki ga Kirei"))
            g.addElo(Graph.Node("feel"), Graph.Node("Hinamatsuri"))
            g.addElo(Graph.Node("feel"), Graph.Node("Dagashi Kashi"))
            g.addElo(Graph.Node("feel"), Graph.Node("Island"))
            g.addElo(Graph.Node("feel"), Graph.Node("Ushinawareta Mirai wo Motomete"))

            g.addElo(Graph.Node("Studio Deen"), Graph.Node("Kono Subarashii Sekai ni Shukufuku wo!"))
            g.addElo(Graph.Node("Studio Deen"), Graph.Node("Sakamoto Desu ga?"))
            g.addElo(Graph.Node("Studio Deen"), Graph.Node("Higurashi no Naku Koro ni"))

            g.addElo(Graph.Node("Sunrise"), Graph.Node("Code Geass"))
            g.addElo(Graph.Node("Sunrise"), Graph.Node("Cowboy Bebop"))
            g.addElo(Graph.Node("Sunrise"), Graph.Node("Gintama"))
            g.addElo(Graph.Node("Sunrise"), Graph.Node("Accel World"))
            g.addElo(Graph.Node("Sunrise"), Graph.Node("Danshi Koukousei no Nichijou"))
            g.addElo(Graph.Node("Sunrise"), Graph.Node("Cross Ange: Tenshi to Ryuu no Rondo"))
            
            g.BFS("Start")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printElos("Start"),
            }

            template = 'search_anime/geral.html'

    return render(request, template, context)