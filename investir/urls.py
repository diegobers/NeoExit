from django.urls import path

from ofertar.models import Oferta

from .views import InvestimentoList, InvestimentoDetail, InvestimentoCreate, InvestimentoUpdate, InvestimentoDelete



urlpatterns = [
    path('', InvestimentoList.as_view(), name='investimentos'),
    path('detalhes/<int:pk>/', InvestimentoDetail.as_view(), name='detalhar-investimento'),
    path('alterar/<int:pk>/', InvestimentoUpdate.as_view(), name='alterar-investimento'),
    path('deletar/<int:pk>/', InvestimentoDelete.as_view(), name='deletar-investimento'),
    path('registrar/<int:oferta_id>/', InvestimentoCreate.as_view(), name='registrar-investimento'),

]       