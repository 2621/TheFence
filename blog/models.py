from django.db import models
from django.utils import timezone
#from ou import adicionam alguns pedaços de outros arquivos

class Post(models.Model):
#models.Model significa que o Post é um modelo de Django, então o Django sabe
#que ele deve ser salvo no banco de dados
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#models.ForeignKey é um link para outro modelo
    title = models.CharField(max_length=200)
#models.CharField define um texto com número limitado de caracteres
    text = models.TextField()
#models.TextFied é para textos sem um limite fixo
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
#__str__ obtem um texto (string)
        return self.title
# Create your models here.
