from django.urls import path
from . import views
from .views import OfertaList, OfertaDetail, OfertaCreate, OfertaUpdate, OfertaDelete


urlpatterns = [
    path('', OfertaList.as_view(), name='ofertas'),
    path('detalhes/<int:pk>/', OfertaDetail.as_view(), name='detalhar-oferta'),
    path('alterar/<int:pk>/', OfertaUpdate.as_view(), name='alterar-oferta'),
    path('deletar/<int:pk>/', OfertaDelete.as_view(), name='deletar-oferta'),
    path('registrar/', OfertaCreate.as_view(), name='registrar-oferta'),

]
