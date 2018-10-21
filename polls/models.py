from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	primeiro_nome = models.CharField(max_length=50, blank=True)
	ultimo_nome = models.CharField(max_length=50, blank=True)
	#ID = models.PositiveIntegerField()
	email = models.EmailField(max_length=30, blank=True)
	#password = models.CharField(max_length=30, blank = False)
	telefone = models.CharField(max_length=50, blank=True)
	aparelho1 = models.CharField(max_length=50, blank=True)
	#aparelho2 = models.CharField(max_length=50, blank=True)
	#aparelho3 = models.CharField(max_length=50, blank=True)
	#colocar campos de position e time (DateField)
	#ver se é aqui que coloca a função para ir atualizando position e time

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
