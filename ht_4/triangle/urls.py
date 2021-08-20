from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='triangle/templates/triangle/index'),
]
