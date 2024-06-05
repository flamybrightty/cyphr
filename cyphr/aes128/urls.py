from django.urls import path
from . import views

app_name = 'aes128'

urlpatterns = [
    path('', views.aes128, name='aes128'),
    path('instruction/', views.instruction, name="instruction"),
    path('cypher/', views.cypher, name='cypher'),
    path('cypher/cypher_result/', views.cypher_result, name='cypher_result'),
    path('decypher/', views.decypher, name='decypher'),
    path('decypher/decypher_result/', views.decypher_result, name='decypher_result'),
]
