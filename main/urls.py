from django.contrib import admin
from django.urls import path, include
from . import views
from .views import EntrarView, CadastrarView#, OfertaDetail
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('entrar/', EntrarView.as_view(), name='entrar'),
    path('cadastrar/', CadastrarView.as_view(), name='cadastrar'),
    path('sair/', LogoutView.as_view(next_page='home'), name='sair'),
    
    path('ofertas/', include('ofertar.urls')),
    path('investimentos/', include('investir.urls')),

    path('', views.home, name='home'),
    #path('detalhes/<int:pk>/', OfertaDetail.as_view() , name='detalhes'),
]
