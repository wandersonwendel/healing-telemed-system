from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastro_medico/', views.cadastro_medico, name="cadastro_medico"),
    path("abrir_horario/", views.abrir_horario, name="abrir_horario")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)