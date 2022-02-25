from django.db import models
from django.contrib.auth.models import User
from ofertar.models import Oferta



class ForumOferta(models.Model):
    cliente = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
    oferta = models.ForeignKey(Oferta, related_name='comentarios', null=True, blank=True, on_delete=models.SET_NULL)
    comentario = models.TextField(null=True, blank=True)    
    data = models.DateField(auto_now_add=True, null=True)   

    def __str__(self):
        return '%s - %s' % (self.cliente.username, self.comentario) 
