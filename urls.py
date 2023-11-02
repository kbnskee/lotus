from django.urls import path
from lotus.views import (
    lotus_app_add,
    lotus_importer,
)

urlpatterns=[
    path('lts/',lotus_app_add,name='lotus_app_add'),
    path('lts/importer/',lotus_importer,name='lotus_importer'),
]