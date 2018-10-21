from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from polls.forms import SignUpForm
from polls.forms import	NovoAparelho

@login_required
def home(request):
	return render(request, 'home.html')

def sobre(request):
	return render(request, 'sobre.html')

def contato(request):
	return render(request, 'contato.html')

def minhaconta(request):
	return render(request, 'minhaconta.html')

def cadastroaparelhos(request):
	if request.method == 'POST':
		form = NovoAparelho(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			#if user.profile.aparelho1 is None:
			user.profile.aparelho1 = form.cleaned_data.get('aparelho1')
			user.save()
			#elif user.profile.aparelho2 is None:
			#	user.profile.aparelho2 = form.cleaned_data.get('aparelho2')
			#	user.save()
			#elif user.profile.aparelho3 is None:
			#	user.profile.aparelho3 = form.cleaned_data.get('aparelho3')
			#	user.save()
		return redirect('minhaconta')
	else:
		form = NovoAparelho()	
	return render(request, 'cadastroaparelhos.html', {'form':form})

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.primeiro_nome = form.cleaned_data.get('primeiro_nome')
			user.save()
			user.profile.ultimo_nome = form.cleaned_data.get('ultimo_nome')
			user.save()
			#user.profile.ID = form.cleaned_data.get('ID')
			#user.save()
			user.profile.email = form.cleaned_data.get('email')
			user.save()
			#user.User.password = form.cleaned_data.get('password')
			#user.save()
			user.profile.telefone = form.cleaned_data.get('telefone')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username,password=raw_password)
			login(request,user)
			return redirect('minhaconta')
	else:
		form = SignUpForm()
	return render (request, 'signup.html', {'form':form})
# Create your views here.
