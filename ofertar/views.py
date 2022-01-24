from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .models import Oferta
from django.urls import reverse_lazy


class OfertaList(ListView):
    model = Oferta
    template_name = 'ofertar/listar.html'
    context_object_name = 'ofertas'


class OfertaDetail(DetailView):
    model = Oferta
    template_name = 'ofertar/detalhes.html'
    context_object_name = 'oferta' 


class OfertaCreate(LoginRequiredMixin, CreateView):
    model = Oferta
    template_name = 'ofertar/registrar.html'
    fields = ['descricao', 'status', 'valor']
    context_object_name = 'oferta'
    success_url = reverse_lazy('ofertas')

    def form_valid(self, form):
        form.instance.cliente = self.request.user
        
        return super(OfertaCreate, self).form_valid(form)


class OfertaUpdate(LoginRequiredMixin, UpdateView):
    model = Oferta
    template_name = 'ofertar/registrar.html'
    context_object_name = 'oferta'
    fields = ['descricao', 'status', 'valor']
    success_url = reverse_lazy('ofertas')


class OfertaDelete(LoginRequiredMixin, DeleteView):
    model = Oferta
    template_name = 'ofertar/deletar.html'
    context_object_name = 'oferta'
    success_url = reverse_lazy('ofertas')
