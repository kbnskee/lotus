from django.urls import path
from lotus.views import (
    lotus_app_list,
    lotus_app_add,
    lotus_app_details,

    lotus_page_list,
    lotus_page_add,
    lotus_page_details,

    lotus_group_list,
    lotus_group_add,
    lotus_group_details,
    lotus_group_app_add,
    lotus_group_page_add,
    lotus_group_app_delete,
    

    lotus_importer,
)

urlpatterns=[
    path('lts/app/list/',lotus_app_list,name='lotus_app_list'),
    path('lts/app/add/',lotus_app_add,name='lotus_app_add'),
    path('lts/app/<int:id>/details/',lotus_app_details,name='lotus_app_details'),
    
    

    path('lts/page/list/',lotus_page_list,name='lotus_page_list'),
    path('lts/page/add/',lotus_page_add,name='lotus_page_add'),
    path('lts/page/<int:id>/details/',lotus_page_details,name='lotus_page_details'),


    path('lts/group/list/',lotus_group_list,name='lotus_group_list'),
    path('lts/group/add/',lotus_group_add,name='lotus_group_add'),
    path('lts/group/<int:id>/details/',lotus_group_details,name='lotus_group_details'),
    path('lts/group/<int:group>/app/add/',lotus_group_app_add,name='lotus_group_app_add'),
    path('lts/group/<int:group>/page/add/',lotus_group_page_add,name='lotus_group_page_add'),
    path('lts/group/<int:group>/app/<int:app>/delete/',lotus_group_app_delete,name='lotus_group_app_delete'),

    path('lts/importer/',lotus_importer,name='lotus_importer'),
]