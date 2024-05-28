from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('index/', views.index, name='index'),
    path('article/', views.article, name='article'),
    path('category', views.category, name='category'),
    path('allnews/', views.allnews, name='allnews'),
    path('about/', views.about, name='about'),
    path('rule/', views.rule, name='rule'),
    path('price/', views.price, name='price'),
    path('conf/', views.confidentiality, name='conf')
]

handler404 = 'myapp.views.custom_404'
