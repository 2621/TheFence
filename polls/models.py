from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	primeiro_nome = models.CharField(max_length=50, blank=True)
	ultimo_nome = models.CharField(max_length=50, blank=True)
	email = models.EmailField(max_length=30, blank=True)
	telefone = models.CharField(max_length=50, blank=True)
#	aparelho = models.CharField(max_length=30, blank=True)
#	ultima_lat = models.CharField(max_length=30, blank=True)
#	ultima_long = models.CharField(max_length=30, blank=True)

class Aparelho(models.Model):
	nome_aparelho = models.CharField(max_length=50, blank=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
