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
    if request.method == 'POST':
        if request.POST.get("bones"):
            print("Bones")
            template = 'search_anime/bones.html'
        elif request.POST.get("wit"):
            print("Wit Studio")
            template = 'search_anime/wit.html'
        elif request.POST.get("mappa"):
            print("Mappa")
            template = 'search_anime/mappa.html'
        elif request.POST.get("madhouse"):
            print("Mad House")
            template = 'search_anime/madhouse.html'
        elif request.POST.get("a1"):
            print("A-1 Pictures")
            template = 'search_anime/apic.html'
        elif request.POST.get("ufotable"):
            print("Ufotable")
            template = 'search_anime/ufotable.html'
        elif request.POST.get("jcstaff"):
            print("J.C Staff")
            template = 'search_anime/jcstaff.html'
        elif request.POST.get("paworks"):
            print("P.A Works")
            template = 'search_anime/paworks.html'
        elif request.POST.get("trigger"):
            print("Trigger")
            template = 'search_anime/trigger.html'
        elif request.POST.get("kyoto"):
            print("Kyoto Animation")
            template = 'search_anime/kyoto.html'
        elif request.POST.get("pierrot"):
            print("Studio Pierrot")
            template = 'search_anime/pierrot.html'
        elif request.POST.get("fox"):
            print("White Fox")
            template = 'search_anime/whitefox.html'
        elif request.POST.get("clover"):
            print("Clover Works")
            template = 'search_anime/clover.html'
        elif request.POST.get("toei"):
            print("Toei Animation")
            template = 'search_anime/toei.html'
        elif request.POST.get("artland"):
            print("Artland")
            template = 'search_anime/artland.html'
        elif request.POST.get("kinema"):
            print("Kinema Citrus")
            template = 'search_anime/kinema.html'
        elif request.POST.get("david"):
            print("David Production")
            template = 'search_anime/david.html'
        elif request.POST.get("voln"):
            print("Studio VOLN")
            template = 'search_anime/voln.html'
        elif request.POST.get("ig"):
            print("Production I.G")
            template = 'search_anime/ig.html'
        elif request.POST.get("gainex"):
            print("Gainex")
            template = 'search_anime/gainax.html'
        elif request.POST.get("tms"):
            print("TMS Entertainment")
            template = 'search_anime/tms.html'
        elif request.POST.get("feel"):
            print("feel")
            template = 'search_anime/feel.html'
        elif request.POST.get("deen"):
            print("Studio Deen")
            template = 'search_anime/deen.html'
        elif request.POST.get("sunrise"):
            print("Sunrise")
            template = 'search_anime/sunrise.html'
    return render(request, template)
