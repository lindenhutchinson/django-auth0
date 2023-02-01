from django.urls import path
from . import views

urlpatterns = [
    path("character/create", views.character_create, name="character_create"),
    path("characters", views.character_list, name="character_list"),
    path("character/<pk>", views.character_detail, name="character_detail"),
    path("character/<pk>/edit", views.character_edit, name="character_edit"),
    path("character/<pk>/delete", views.character_delete, name="character_delete"),
]
