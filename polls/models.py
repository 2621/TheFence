from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	primeiro_nome = models.CharField(max_length=50, blank=True)
	ultimo_nome = models.CharField(max_length=50, blank=True)
	email = models.EmailField(max_length=30, blank=True)
	telefone = models.CharField(max_length=50, blank=True)
	nome_aparelho = models.CharField(max_length=30, blank=True)
	ultima_lat = models.CharField(max_length=30, blank=True, null=True)
	ultima_long = models.CharField(max_length=30, blank=True, null=True)

#class Aparelho(models.Model):
#	nome_aparelho = models.CharField(max_length=50, blank=True)
#	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Limite_Bairro(models.Model):
	gid = models.IntegerField(primary_key=True)
	objectid = models.BigIntegerField(blank=True)
	Área = models.DecimalField(max_digits=None, decimal_places=None, blank=True)
	nome = models.CharField(max_length=80, blank=True)
	regiao_adm = models.CharField(max_length=80, blank=True)
	area_plane = models.CharField(max_length=80, blank=True)
	codbairro = models.CharField(max_length=80, blank=True)
	codra = models.BigIntegerField(blank=True)
	codbnum = models.BigIntegerField(blank=True)
	link = models.CharField(max_length=80, blank=True)
	shapestare = models.DecimalField(max_digits=None, decimal_places=None, blank=True)
	shapestlen = models.DecimalField(max_digits=None, decimal_places=None, blank=True)
	rp = models.CharField(max_length=80, blank=True)
	cod_rp = models.CharField(max_length=80, blank=True)
	codbairro_ = models.BigIntegerField(blank=True)
	geom = models.MultiPolygonField()
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
