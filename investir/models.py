from django.db import models
from django.contrib.auth.models import User
from ofertar.models import Oferta


STATUS = [
    ('Solicitado','Solicitado'),
    ('Em Andamento','Em Andamento'),
    ('Aprovado','Aprovado'),
    ('Finalizado','Finalizado'),
]

class Investimento(models.Model):
    cliente = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) 
    data_criacao = models.DateField(auto_now_add=True, null=True)
    oferta = models.ForeignKey(Oferta, null=True, on_delete=models.SET_NULL, blank=True )
    valor = models.DecimalField(null=True, max_digits=9, decimal_places=2)    
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='Solicitado')
  
    class Meta:
        ordering = ['valor']   

