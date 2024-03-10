from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('upload/', views.upload, name='upload'),
    path('tag/', views.tag, name='tag'),

]
