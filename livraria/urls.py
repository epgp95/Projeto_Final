from django.contrib import admin
from django.urls import path, include
from livros import views as livros_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('livros.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registo/', livros_views.registo, name='registo'),
]