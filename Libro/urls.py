"""Libro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path
from django.conf.urls import include, url
from proyecto import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as viewss
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [ 
    path('accounts/login/', viewss.LoginView.as_view(template_name='Registro/login.html'), name='login'),
    path('accounts/logout/', viewss.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    path('',views.home, name='home'),
    #urls Autor
    path('autor', views.autor, name='autor_index'),
    path('autor/nuevo', views.autor_nuevo, name='autor_nuevo'),
    path('autor/(?P<pk>[0-9]+)/editar/', views.autor_edit, name='autor_editar'),
    path('autor/show/(?P<pk>[0-9]+)/', views.autor_show, name='autor_show'),
    path('autor/(?P<pk>[0-9]+)/remove/', views.autor_remove, name='autor_remove'),
    

     #urls Pais
    path('pais', views.pais, name='pais_index'),
    path('pais/nuevo', views.pais_nuevo, name='pais_nuevo'),
    path('pais/(?P<pk>[0-9]+)/editar/', views.pais_edit, name='pais_editar'),
    path('pais/show/(?P<pk>[0-9]+)/', views.pais_show, name='pais_show'),
    path('pais/(?P<pk>[0-9]+)/remove/', views.pais_remove, name='pais_remove'),
    
    #urls Libro
    path('libro', views.libro, name='libro_index'), 
    path('libro/nuevo', views.libro_nuevo, name='libro_nuevo'),
    path('libro/(?P<pk>[0-9]+)/editar/', views.libro_editar, name='libro_editar'),
    path('libro/(?P<pk>\d+)/remove/', views.libro_remove, name='libro_remove'),
        #urls Categoria
    path('categoria', views.categoria, name='categoria_index'),
    path('categoria/nuevo', views.categoria_nuevo, name='categoria_nuevo'), 
    path('categoria/(?P<pk>[0-9]+)/editar/', views.categoria_edit, name='categoria_editar'),
    path('categoria/show/(?P<pk>[0-9]+)/', views.categoria_show, name='categoria_show'),
    path('categoria/(?P<pk>[0-9]+)/remove/', views.categoria_remove, name='categoria_remove'),

    #administrador
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

