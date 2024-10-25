from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("add/", views.add, name="add"),
    path("api/recipe", views.get_recipe.as_view(http_method_names=['post']), name="api recipy"),
]
