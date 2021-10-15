from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('domande', views.domande, name='domande'),
    path('domanda/<int:q_id>', views.dettaglio, name='dettaglio')
]