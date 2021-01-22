from django.urls import path
from . import views
urlpatterns = [path('', views.home, name='home'),
               #    path('add', views.add_get, name='add'),
               path('add', views.add_post, name='add')]
