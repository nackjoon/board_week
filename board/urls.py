from django.urls import path
from . import views

app_name="board"
urlpatterns = [
    path('', views.index,name="index"),
    path('createBoard/', views.createBoard,name="createBoard"),
    path('detail/<bpk>',views.detail,name="detail"),
    path('deleteBoard/<bpk>',views.deleteBoard,name="deleteBoard"),
    path('modifyBoard/<bpk>',views.modifyBoard,name="modifyBoard"),
    path('addHeart/<bpk>',views.addHeart,name="addHeart"),
    path('removeHeart/<bpk>',views.removeHeart,name="removeHeart"),
    
]
