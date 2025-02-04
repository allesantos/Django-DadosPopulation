from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rota para a página principal
    path('get-data/', views.get_data, name='get_data'),  # Rota para obter os dados da API em JSON
]
