from django.urls import path
from . import views


urlpatterns = [
    path('',                views.Home,    name='home'),
    path('create',          views.Create,  name='create'),
    path('vote/<str:pk>',   views.Vote,    name='vote'),
    path('result/<str:pk>', views.Result,  name='result'),

]