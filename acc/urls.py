from django.urls import path
from . import views

app_name="acc"
urlpatterns = [
    path('', views.index,name="index"),
    path('member/userlogin/', views.userlogin,name="userlogin"),
    path('member/userJoin/',views.userJoin,name="userJoin"),
    path('member/userLogout/',views.userLogout,name="userLogout"),
    path('member/userInfo/', views.userInfo,name="userInfo"),
    path('member/userUpdate/', views.userUpdate,name="userUpdate"),
    path('member/userDel/',views.userDel,name="userDel")
]
