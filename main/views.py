from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from ofertar.models import Oferta
#from django.views.generic.detail import DetailView


def home(request):
    ofertas = Oferta.objects.all()
    context = {'oferta':ofertas}

    return render(request, 'home.html', context)


#class OfertaDetail(DetailView):
#    model = Oferta
#    template_name = 'ofertar/detalhes.html'
#    context_object_name = 'oferta'


class EntrarView(LoginView):
    template_name = 'main/entrar.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class CadastrarView(FormView):
    template_name = 'main/cadastrar.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CadastrarView, self).form_valid(form)
    # return view if is_authenticated
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')    
        return super(CadastrarView, self).get(*args, **kwargs)    