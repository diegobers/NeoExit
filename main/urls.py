from django.contrib import admin
from django.urls import path, include
from . import views
from .views import EntrarView, CadastrarView#, OfertaDetail
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entrar/', EntrarView.as_view(), name='entrar'),
    path('cadastrar/', CadastrarView.as_view(), name='cadastrar'),
    path('sair/', LogoutView.as_view(next_page='home'), name='sair'),
    path('', views.home, name='home'),
    
    path('ofertas/', include('ofertar.urls')),
    path('investimentos/', include('investir.urls')),
    #path('detalhes/<int:pk>/', OfertaDetail.as_view() , name='detalhes'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

