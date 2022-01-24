from django.db import models

GRUPO = [
    ('Destaque','Destaque'),
    ('Aberta','Aberta'),
    ('Fechada','Fechada'),
]

class Oferta(models.Model):
    descricao = models.CharField(max_length=200, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    valor = models.FloatField(null=True)
    status = models.CharField(max_length=200, null=True, choices=GRUPO)   

    def __str__(self):
        return self.descricao 

    class Meta:
        ordering = ['data_criacao']   
 
