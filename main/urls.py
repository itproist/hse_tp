from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("api/recipy", views.get_recipy, name="api recipy"),
]
