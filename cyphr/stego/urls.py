from django.urls import path
from . import views

app_name = "stego"

urlpatterns = [
    path('', views.stego, name="stego"),
    path('instruction/', views.instruction, name="instruction"),
    path('hide/', views.hide, name="hide"),
    path('extract/', views.extract, name="extract"),
    path('extract/result/', views.extract_result, name="extract_result"),
    path('result/', views.result, name="result"),
]
