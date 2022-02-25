from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from .models import ForumOferta
from ofertar.models import Oferta


class ForumOfertaList(ListView):
    model = ForumOferta
    template_name = 'forum/listar.html'
    context_object_name = 'forum'       

class ForumOfertaCreate(CreateView):
    model = ForumOferta
    template_name = 'ofertar/forum.html' 
    fields = ['comentario']   
    context_object_name = 'forum'  
    
    def dispatch(self, request, *args, **kwargs):
        self.oferta_id = get_object_or_404(Oferta, pk=kwargs['oferta_id'])
        print(self.oferta_id)
        print('-----------1')
        print(self.oferta_id.pk)
        
        return super(ForumOfertaCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print('-----------3')
        print(self.oferta_id.pk)
        form.instance.cliente = self.request.user 
        form.instance.oferta_id = self.oferta_id.pk
        
        return super(ForumOfertaCreate, self).form_valid(form)
