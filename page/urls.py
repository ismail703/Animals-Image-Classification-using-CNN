from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("marine/", views.marine, name="marine"),
    path("replite/", views.replite, name="replite"),
    path("birds/", views.bird, name="birds"),
    path("wild/", views.wild, name="wild"),
    path("unknown/", views.unknown, name="unknown"),
]