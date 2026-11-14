from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('<int:member_id>', views.member_detail, name='member_detail'),
    path('info/', views.member_info, name='member_info'),
]