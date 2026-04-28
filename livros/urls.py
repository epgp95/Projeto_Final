from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_livros, name="lista_livros"),
    path("novo/", views.adicionar_livro, name="adicionar_livro"),
    path("toggle/<int:id>/", views.toggle_vendido, name="toggle_vendido"),
    path("editar/<int:id>/", views.livro_update, name="livro_update"),
    path("apagar/<int:id>/", views.livro_delete, name="livro_delete"),
]