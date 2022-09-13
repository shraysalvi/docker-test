from django.urls import path, include
from . import views

urlpatterns = [path("done", views.test, name='test'), path("", views.index)]
