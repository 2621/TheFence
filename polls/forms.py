from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from polls.models import Aparelho


class SignUpForm(UserCreationForm):
	primeiro_nome = forms.CharField(max_length=50)
	ultimo_nome = forms.CharField(max_length=50)
	#ID = forms.IntegerField()
	email = forms.EmailInput()
	#password = forms.CharField(max_length=30, blank = False)
	telefone = forms.CharField(max_length=50)

	class Meta:
		model = User
		fields = ('username', 'primeiro_nome', 'ultimo_nome', 'email', 'telefone', 'password1', 'password2',)

class NovoAparelho(forms.ModelForm):
	aparelho = forms.CharField(max_length=50)

	class Meta:
		model = User
		fields = ('aparelho',)
		