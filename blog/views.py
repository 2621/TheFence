from django.shortcuts import render
def index(request):
    return render(request, 'index/index.html', {})

def sobre(request):
    return render(request, 'sobre/sobre.html', {})

def contato(request):
    return render(request, 'contato/contato.html', {})

def singup(request):
    return render(request, 'singup/singup.html', {})
#render= exibir, gerar tela

# Create your views here.
