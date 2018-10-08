from django.shortcuts import render
def index(request):
    return render(request, 'index/index.html', {})
def sobre(request):
    return render(request, 'sobre/sobre.html', {})

# Create your views here.
