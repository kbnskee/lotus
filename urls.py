from django.urls import path
from lotus.views import (
    lotus_app_list,
    lotus_app_add,
    lotus_app_details,

    lotus_page_list,
    lotus_page_add,

    lotus_group_list,
    lotus_group_add,

    lotus_importer,
)

urlpatterns=[
    path('lts/app/list/',lotus_app_list,name='lotus_app_list'),
    path('lts/app/add/',lotus_app_add,name='lotus_app_add'),
    path('lts/app/<int:id>/details/',lotus_app_details,name='lotus_app_details'),

    path('lts/page/list/',lotus_page_list,name='lotus_page_list'),
    path('lts/page/add/',lotus_page_add,name='lotus_page_add'),

    path('lts/group/list/',lotus_group_list,name='lotus_group_list'),
    path('lts/group/add/',lotus_group_add,name='lotus_group_add'),

    path('lts/importer/',lotus_importer,name='lotus_importer'),
]