from django.urls import path
from . import views

urlpatterns = [
    path('api/spells/<int:spell_id>/description/', views.spell_description),
    path('spells', views.spell_table, name="spell_table")
]
