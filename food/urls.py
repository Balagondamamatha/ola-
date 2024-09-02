from django.urls import path
from food.views import *
app_name='foodie'
urlpatterns=[
    path('biryani/',biryani,name='biryani')
]