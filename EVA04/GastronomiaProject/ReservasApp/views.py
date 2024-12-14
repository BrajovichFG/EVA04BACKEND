from django.shortcuts import render
from ReservasApp.models import Reserva

def index(request):
    return render(request, 'index.html')


def reservasList(request):
    reservas = Reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'ReservasTemplates/reservas.html', data)

# Create your views here.
