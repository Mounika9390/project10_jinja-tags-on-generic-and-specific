from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('anusha/',anusha,name='anusha'),
    path('mouni/',mouni,name='mouni')
]