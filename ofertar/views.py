from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin
from django.views.generic.detail import DetailView
from .models import Oferta
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden


class OfertaList(ListView):
    model = Oferta
    template_name = 'ofertar/listar.html'
    context_object_name = 'ofertas'

class OfertaCreate(LoginRequiredMixin, CreateView):
    model = Oferta
    template_name = 'ofertar/registrar.html'
    fields = ['descricao', 'status', 'valor', 'img']
    context_object_name = 'oferta'
    success_url = reverse_lazy('ofertas')

    def form_valid(self, form):
        form.instance.cliente = self.request.user
        form.instance.img = self.request.FILES
        
        return super(OfertaCreate, self).form_valid(form)

class OfertaUpdate(LoginRequiredMixin, UpdateView):
    model = Oferta
    template_name = 'ofertar/registrar.html'
    context_object_name = 'oferta'
    fields = ['descricao', 'status', 'valor', 'img']
    success_url = reverse_lazy('ofertas')

class OfertaDelete(LoginRequiredMixin, DeleteView):
    model = Oferta
    template_name = 'ofertar/deletar.html'
    context_object_name = 'oferta'
    success_url = reverse_lazy('ofertas')

class OfertaDetail(DetailView):
    model = Oferta
    template_name = 'ofertar/detalhes.html'
    context_object_name = 'oferta'
       




#def get_context_data(self, **kwargs):
#    context = super(ForumOfertaFormView, self).get_context_data(**kwargs)
#    context['form'] = self.get_form()
#    return context
#def post(self, request, *args, **kwargs):
#    self.object = self.get_object()
#    form = self.get_form() 
#    print(form.instance.cliente_id)
#    if form.is_valid():
#        return self.form_valid(form)
#    else:
#        return self.form_invalid(form)

#class OfertaDetailView(View):
#
#    def get(self, request, *args, **kwargs):
#        view = OfertaDetailView.as_view()
#        return view(request, *args, **kwargs)
#
#    def post(self, request, *args, **kwargs):
#        view = ForumOfertaFormView.as_view()
#        return view(request, *args, **kwargs)
 



 