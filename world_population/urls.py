from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('population.urls')),  # Incluindo URLs do app population
    path('', RedirectView.as_view(url='/')),  # Redirecionamento para a página principal
]


