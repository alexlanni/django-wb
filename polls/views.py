from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Domanda


def index(request):
    return HttpResponse("Che spettacolo")

def domande(request):

    ultime_domande = Domanda.objects.order_by('-data')[:5]

    context = {'ultime_domande': ultime_domande}

    ##template = loader.get_template('polls/domande.html')
    ##return HttpResponse(template.render(context, request))

    return render(request, 'polls/domande.html', context)

def dettaglio(request, q_id):
    try:
        domanda = Domanda.objects.get(pk=q_id)
    except Domanda.DoesNotExist:
        raise Http404("Domanda non trovata")
    return render(request, 'polls/detail.html', {'domanda': domanda})
