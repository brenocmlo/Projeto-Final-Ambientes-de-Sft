from django.urls import path
from app_cad_user import views
urlpatterns = [
    path('', views.inicial, name='inicial'),
    path('usuarios/', views.usuario, name='listagem_user'),
]
