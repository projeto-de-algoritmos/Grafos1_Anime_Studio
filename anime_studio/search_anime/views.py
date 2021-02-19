from django.shortcuts import render
from django.http import HttpResponse
from search_anime.util import BFS

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

def projeto(request):
    g = BFS.Grafo()
    template = 'search_anime/projeto.html'
    context = {}
    if request.method == 'POST':
        if request.POST.get("bones"):
            g.addElo(BFS.Node("Bones"), BFS.Node("Fullmetal Alchemist: Brotherhood"))
            g.addElo(BFS.Node("Bones"), BFS.Node("Boku no Hero Academia"))
            g.addElo(BFS.Node("Bones"), BFS.Node("Noragami"))
            g.addElo(BFS.Node("Bones"), BFS.Node("Mob Psycho 100"))
            g.addElo(BFS.Node("Bones"), BFS.Node("Soul Eater"))
            g.addElo(BFS.Node("Bones"), BFS.Node("Bungou Stray Dogs"))
            g.addElo(BFS.Node("Bones"), BFS.Node("Darker than Black"))
            g.addElo(BFS.Node("Bones"), BFS.Node("Kekkai Sensen"))
            g.addElo(BFS.Node("Bones"), BFS.Node("Carole & Tuesday"))

            g.BFS("Bones")
            g.plotGraph()
            # g.printLayers()

            context =  {
                'nosso_grafo': g.printGraph(),
                # 'distancia_grafo': g.printLayers(),
            }


            template = 'search_anime/bones.html'

        elif request.POST.get("wit"):
            g.addElo(BFS.Node("Wit Studio"), BFS.Node("Shingeki no Kyojin(1 - 3)"))
            g.addElo(BFS.Node("Wit Studio"), BFS.Node("Owari no Seraph"))
            g.addElo(BFS.Node("Wit Studio"), BFS.Node("Vinland Saga"))
            g.addElo(BFS.Node("Wit Studio"), BFS.Node("Koutetsujou no Kabaneri"))
            g.addElo(BFS.Node("Wit Studio"), BFS.Node("Mahoutsukai no Yome"))
            g.addElo(BFS.Node("Wit Studio"), BFS.Node("Great Pretender"))
            g.addElo(BFS.Node("Wit Studio"), BFS.Node("Koi wa Ameagari no You ni"))

            g.BFS("Wit Studio")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            
            template = 'search_anime/wit.html'

        elif request.POST.get("mappa"):
            g.addElo(BFS.Node("Mappa"), BFS.Node("Shingeki no Kyojin(4)"))
            g.addElo(BFS.Node("Mappa"), BFS.Node("Kakegurui"))
            g.addElo(BFS.Node("Mappa"), BFS.Node("Zankyou no Terror"))
            g.addElo(BFS.Node("Mappa"), BFS.Node("Dororo"))
            g.addElo(BFS.Node("Mappa"), BFS.Node("Jujutsu Kaisen"))
            g.addElo(BFS.Node("Mappa"), BFS.Node("The God of High School"))
            g.addElo(BFS.Node("Mappa"), BFS.Node("Inuyashiki"))
            g.addElo(BFS.Node("Mappa"), BFS.Node("Dorohedoro"))
            g.addElo(BFS.Node("Mappa"), BFS.Node("Ushio to Tora"))

            g.BFS("Mappa")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/mappa.html'

        elif request.POST.get("madhouse"):
            g.addElo(BFS.Node("Mad House"), BFS.Node("Death Note"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("One Punch Man"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("No Game No Life"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Hunter x Hunter (2011)"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Kiseijuu: Sei no Kakuritsu"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Death Parade"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Highschool of the Dead"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Overlord"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Mahouka Koukou no Rettousei"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Black Lagoon"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Btooom!"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Hellsing Ultimate"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Monster"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Claymore"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Ore Monogatari!!"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Hajime no Ippo"))
            g.addElo(BFS.Node("Mad House"), BFS.Node("Paprika"))

            g.BFS("Mad House")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/madhouse.html'

        elif request.POST.get("a1"):
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Darling in the FranXX"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Sword Art Online"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Shigatsu wa Kimi no Uso"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Ao no Exorcist"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Nanatsu no Taizai"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Boku dake ga Inai Machi"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Fairy Tail"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Magi: The Labyrinth of Magic"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Gate: Jieitai Kanochi nite, Kaku Tatakaeri"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Hai to Gensou no Grimgar"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Wotaku ni Koi wa Muzukashii"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Gakusen Toshi Asterisk"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Blend S"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Saenai Heroine no Sodatekata"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Aldnoah.Zero"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Ore no Kanojo to Osananajimi ga Shuraba Sugiru"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Ore no Imouto ga Konnani Kawaii Wake ga Nai"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Working!!"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Demi-chan wa Kataritai"))
            g.addElo(BFS.Node("A-1 Pictures"), BFS.Node("Grancrest Senki"))
            
            g.BFS("A-1 Pictures")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/apic.html'

        elif request.POST.get("ufotable"):
            g.addElo(BFS.Node("Ufotable"), BFS.Node("Kimetsu no Yaiba"))
            g.addElo(BFS.Node("Ufotable"), BFS.Node("Fate/Zero"))
            g.addElo(BFS.Node("Ufotable"), BFS.Node("God Eater"))

            g.BFS("Ufotable")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/ufotable.html'

        elif request.POST.get("jcstaff"):
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Toradora!"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Shokugeki no Souma"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Sakura-sou no Pet na Kanojo"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Kaichou wa Maid-sama!"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Prison School"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Golden Time"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Zero no Tsukaima"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Toaru Majutsu no Index"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Saiki Kusuo no Ψ-nan"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Bakuman"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("High Score Girl"))
            g.addElo(BFS.Node("JC Staff"), BFS.Node("Back Street Girls: Gokudolls"))
            
            g.BFS("JC Staff")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/jcstaff.html'

        elif request.POST.get("paworks"):
            g.addElo(BFS.Node("PA Works"), BFS.Node("Angel Beats!"))
            g.addElo(BFS.Node("PA Works"), BFS.Node("Another"))
            g.addElo(BFS.Node("PA Works"), BFS.Node("Charlotte"))
            g.addElo(BFS.Node("PA Works"), BFS.Node("Nagi no Asu kara"))
            g.addElo(BFS.Node("PA Works"), BFS.Node("Hanasaku Iroha"))
            g.addElo(BFS.Node("PA Works"), BFS.Node("Kamisama ni Natta Hi"))
            
            g.BFS("PA Works")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/paworks.html'

        elif request.POST.get("trigger"):
            g.addElo(BFS.Node("Trigger"), BFS.Node("Kill la Kill"))
            g.addElo(BFS.Node("Trigger"), BFS.Node("Darling in the FranXX"))
            g.addElo(BFS.Node("Trigger"), BFS.Node("Kiznaiver"))
            g.addElo(BFS.Node("Trigger"), BFS.Node("Little Witch Academia"))
            g.addElo(BFS.Node("Trigger"), BFS.Node("SSSS.Gridman"))
            g.addElo(BFS.Node("Trigger"), BFS.Node("BNA: Brand New Animal"))

            g.BFS("Trigger")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/trigger.html'

        elif request.POST.get("kyoto"):
            g.addElo(BFS.Node("Kyoto Animation"), BFS.Node("Clannad"))
            g.addElo(BFS.Node("Kyoto Animation"), BFS.Node("Violet Evergarden"))
            g.addElo(BFS.Node("Kyoto Animation"), BFS.Node("Chuunibyou demo Koi ga Shitai!"))
            g.addElo(BFS.Node("Kyoto Animation"), BFS.Node("Hyouka"))
            g.addElo(BFS.Node("Kyoto Animation"), BFS.Node("Kyoukai no Kanata"))
            g.addElo(BFS.Node("Kyoto Animation"), BFS.Node("K-On!"))
            g.addElo(BFS.Node("Kyoto Animation"), BFS.Node("Kobayashi-san Chi no Maid Dragon"))
            g.addElo(BFS.Node("Kyoto Animation"), BFS.Node("Suzumiya Haruhi no Yuuutsu"))
            g.addElo(BFS.Node("Kyoto Animation"), BFS.Node("Nichijou"))
            g.addElo(BFS.Node("Kyoto Animation"), BFS.Node("Amagi Brilliant Park"))

            g.BFS("Kyoto Animation")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/kyoto.html'

        elif request.POST.get("pierrot"):
            g.addElo(BFS.Node("Studio Pierrot"), BFS.Node("Tokyo Ghoul"))
            g.addElo(BFS.Node("Studio Pierrot"), BFS.Node("Naruto"))
            g.addElo(BFS.Node("Studio Pierrot"), BFS.Node("Naruto: Shippuuden"))
            g.addElo(BFS.Node("Studio Pierrot"), BFS.Node("Bleach"))
            g.addElo(BFS.Node("Studio Pierrot"), BFS.Node("Black Clover"))
            g.addElo(BFS.Node("Studio Pierrot"), BFS.Node("Yuu☆Yuu☆Hakusho"))
            g.addElo(BFS.Node("Studio Pierrot"), BFS.Node("Akudama Drive"))
            g.addElo(BFS.Node("Studio Pierrot"), BFS.Node("Great Teacher Onizuka"))

            g.BFS("Studio Pierrot")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/pierrot.html'

        elif request.POST.get("fox"):
            g.addElo(BFS.Node("White Fox"), BFS.Node("Steins;Gate"))
            g.addElo(BFS.Node("White Fox"), BFS.Node("Re:Zero kara Hajimeru Isekai Seikatsu"))
            g.addElo(BFS.Node("White Fox"), BFS.Node("Akame ga Kill!"))
            g.addElo(BFS.Node("White Fox"), BFS.Node("Hataraku Maou-sama!"))
            g.addElo(BFS.Node("White Fox"), BFS.Node("Goblin Slayer"))
            g.addElo(BFS.Node("White Fox"), BFS.Node("Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru"))
            g.addElo(BFS.Node("White Fox"), BFS.Node("Arifureta Shokugyou de Sekai Saikyou"))
            
            g.BFS("White Fox")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/whitefox.html'

        elif request.POST.get("clover"):
            g.addElo(BFS.Node("Clover Works"), BFS.Node("Yakusoku no Neverland"))
            g.addElo(BFS.Node("Clover Works"), BFS.Node("Darling in the FranXX"))
            g.addElo(BFS.Node("Clover Works"), BFS.Node("Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai"))
            g.addElo(BFS.Node("Clover Works"), BFS.Node("Horimiya"))
            g.addElo(BFS.Node("Clover Works"), BFS.Node("Wonder Egg Priority"))
            g.addElo(BFS.Node("Clover Works"), BFS.Node("Persona 5 the Animation"))
            
            g.BFS("Clover Works")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/clover.html'

        elif request.POST.get("toei"):
            g.addElo(BFS.Node("Toei Animation"), BFS.Node("One Piece"))
            g.addElo(BFS.Node("Toei Animation"), BFS.Node("DragonBall Z"))
            g.addElo(BFS.Node("Toei Animation"), BFS.Node("Digimon"))
            g.addElo(BFS.Node("Toei Animation"), BFS.Node("Yu☆Gi☆Oh!"))
            
            g.BFS("Toei Animation")
            g.plotGraph()
            
            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/toei.html'

        elif request.POST.get("artland"):
            g.addElo(BFS.Node("Artland"), BFS.Node("Mushishi"))

            g.BFS("Artland")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/artland.html'

        elif request.POST.get("kinema"):
            g.addElo(BFS.Node("Kinema Citrus"), BFS.Node("Tate no Yuusha no Nariagari"))
            g.addElo(BFS.Node("Kinema Citrus"), BFS.Node("Made in Abyss"))
            g.addElo(BFS.Node("Kinema Citrus"), BFS.Node("Black Bullet"))
            g.addElo(BFS.Node("Kinema Citrus"), BFS.Node("Barakamon"))

            g.BFS("Kinema Citrus")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/kinema.html'
        elif request.POST.get("david"):
            g.addElo(BFS.Node("David Production"), BFS.Node("JoJo no Kimyou na Bouken"))
            g.addElo(BFS.Node("David Production"), BFS.Node("JoJo no Kimyou na Bouken Part 3: Stardust Crusaders"))
            g.addElo(BFS.Node("David Production"), BFS.Node("JoJo no Kimyou na Bouken Part 4: Diamond wa Kudakenai"))
            g.addElo(BFS.Node("David Production"), BFS.Node("JoJo no Kimyou na Bouken Part 5: Ougon no Kaze"))
            g.addElo(BFS.Node("David Production"), BFS.Node("Enen no Shouboutai"))
            g.addElo(BFS.Node("David Production"), BFS.Node("Hataraku Saibou"))

            g.BFS("David Production")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/david.html'

        elif request.POST.get("voln"):
            g.addElo(BFS.Node("Studio VOLN"), BFS.Node("Ushio to Tora"))
            g.addElo(BFS.Node("Studio VOLN"), BFS.Node("Karakuri Circus"))

            g.BFS("Studio Deen")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/voln.html'

        elif request.POST.get("ig"):
            g.addElo(BFS.Node("Production IG"), BFS.Node("Psycho-Pass"))
            g.addElo(BFS.Node("Production IG"), BFS.Node("Haikyuu!!"))
            g.addElo(BFS.Node("Production IG"), BFS.Node("Kuroko no Basket"))
            g.addElo(BFS.Node("Production IG"), BFS.Node("Guilty Crown"))
            g.addElo(BFS.Node("Production IG"), BFS.Node("Yuukoku no Moriarty"))

            g.BFS("Production IG")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/ig.html'

        elif request.POST.get("gainex"):
            g.addElo(BFS.Node("Gainex"), BFS.Node("Tengen Toppa Gurren Lagann"))
            g.addElo(BFS.Node("Gainex"), BFS.Node("Neon Genesis Evangelion"))

            g.BFS("Gainex")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/gainax.html'

        elif request.POST.get("tms"):
            g.addElo(BFS.Node("TMS Entertainment"), BFS.Node("Dr. Stone"))
            g.addElo(BFS.Node("TMS Entertainment"), BFS.Node("ReLIFE"))
            g.addElo(BFS.Node("TMS Entertainment"), BFS.Node("D.Gray-man"))
            g.addElo(BFS.Node("TMS Entertainment"), BFS.Node("Kanojo, Okarishimasu"))
            g.addElo(BFS.Node("TMS Entertainment"), BFS.Node("Fruits Basket"))
            g.addElo(BFS.Node("TMS Entertainment"), BFS.Node("Baki"))
            g.addElo(BFS.Node("TMS Entertainment"), BFS.Node("Zetman"))
            g.addElo(BFS.Node("TMS Entertainment"), BFS.Node("Saint Seiya: The Lost Canvas - Meiou Shinwa"))
            g.addElo(BFS.Node("TMS Entertainment"), BFS.Node("Bakugan"))
            g.addElo(BFS.Node("TMS Entertainment"), BFS.Node("Tottoko Hamtarou"))

            g.BFS("TMS Entertainment")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/tms.html'

        elif request.POST.get("feel"):
            g.addElo(BFS.Node("feel"), BFS.Node("Yahari Ore no Seishun Love Comedy wa Machigatteiru. Zoku"))
            g.addElo(BFS.Node("feel"), BFS.Node("Tsuki ga Kirei"))
            g.addElo(BFS.Node("feel"), BFS.Node("Hinamatsuri"))
            g.addElo(BFS.Node("feel"), BFS.Node("Dagashi Kashi"))
            g.addElo(BFS.Node("feel"), BFS.Node("Island"))
            g.addElo(BFS.Node("feel"), BFS.Node("Ushinawareta Mirai wo Motomete"))

            g.BFS("feel")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/feel.html'

        elif request.POST.get("deen"):
            g.addElo(BFS.Node("Studio Deen"), BFS.Node("Kono Subarashii Sekai ni Shukufuku wo!"))
            g.addElo(BFS.Node("Studio Deen"), BFS.Node("Sakamoto Desu ga?"))
            g.addElo(BFS.Node("Studio Deen"), BFS.Node("Higurashi no Naku Koro ni"))

            g.BFS("Studio Deen")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/deen.html'

        elif request.POST.get("sunrise"):
            g.addElo(BFS.Node("Sunrise"), BFS.Node("Code Geass"))
            g.addElo(BFS.Node("Sunrise"), BFS.Node("Cowboy Bebop"))
            g.addElo(BFS.Node("Sunrise"), BFS.Node("Gintama"))
            g.addElo(BFS.Node("Sunrise"), BFS.Node("Accel World"))
            g.addElo(BFS.Node("Sunrise"), BFS.Node("Danshi Koukousei no Nichijou"))
            g.addElo(BFS.Node("Sunrise"), BFS.Node("Cross Ange: Tenshi to Ryuu no Rondo"))

            g.BFS("Sunrise")
            g.plotGraph()

            context =  {
                'nosso_grafo': g.printGraph(),
            }
            template = 'search_anime/sunrise.html'

    return render(request, template, context)
