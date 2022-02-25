from time import process_time_ns
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy

from ofertar.models import Oferta

from .models import Investimento

class InvestimentoList(LoginRequiredMixin, ListView):
    model = Investimento
    template_name = 'investir/listar.html'
    context_object_name = 'investimentos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_staff:
            context['investimentos'] = context['investimentos'].filter(cliente=self.request.user)
        return context

class InvestimentoDetail(LoginRequiredMixin, DetailView):
    model = Investimento
    template_name = 'investir/detalhes.html'
    context_object_name = 'investimento'


class InvestimentoCreate(LoginRequiredMixin, CreateView):
    model = Investimento
    template_name = 'investir/registrar.html'
    fields = ['valor']
    context_object_name = 'investimento'
    success_url = reverse_lazy('investimentos')

    def dispatch(self, request, *args, **kwargs):
        self.oferta_id = get_object_or_404(Oferta, pk=kwargs['oferta_id'])
        return super(InvestimentoCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.cliente = self.request.user   
        form.instance.oferta_id = self.oferta_id.pk
        
        return super(InvestimentoCreate, self).form_valid(form)

class InvestimentoUpdate(LoginRequiredMixin, UpdateView):
    model = Investimento
    template_name = 'investir/registrar.html'
    fields = ['oferta', 'valor', 'status']
    context_object_name = 'investimento'
    success_url = reverse_lazy('investimentos')


class InvestimentoDelete(LoginRequiredMixin, DeleteView):
    model = Investimento
    template_name = 'investir/deletar.html'
    context_object_name = 'investimento'
    success_url = reverse_lazy('investimentos')

