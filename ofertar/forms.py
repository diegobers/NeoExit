from django import forms
from .models import ForumOferta

class ForumForm(forms.Form):

    class Meta:
        model = ForumOferta
        fields = 'comentario'