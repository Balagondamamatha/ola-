from django.urls import path
from  travel.views import *
app_name='traveller'
urlpatterns=[
    path('hyderabad/',hyderabad,name='hyderabad')
]