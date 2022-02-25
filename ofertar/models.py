from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import User


GRUPO = [
    ('Destaque','Destaque'),
    ('Aberta','Aberta'),
    ('Fechada','Fechada'),
]

class Oferta(models.Model):
    descricao = models.CharField(max_length=200, null=True)
    data_criacao = models.DateField(auto_now_add=True, null=True)
    valor = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    status = models.CharField(max_length=200, null=True, choices=GRUPO) 
    img = models.ImageField(null=True, blank=True, upload_to='img/')  

    def __str__(self):
        return self.descricao 

    class Meta:
        ordering = ['descricao']   
