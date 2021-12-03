from django.shortcuts import render

# Create your views here.

def bienvenida(request):
    return render(request, "inicio/index.html", {})

def contactos(request):
    contexto = {'nombre': 'axel',
                'lista_numeros': [500, 1700, 2000],
                'edad': 15
                }
                
    return render(request, "inicio/contactos.html", contexto)
