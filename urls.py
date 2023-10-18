from django.urls import path
from lotus.views import (
    lotus_app_add,
    lotus_app_list
)

urlpatterns=[
    path('lts/',lotus_app_add,name='lotus_app_add'),
]