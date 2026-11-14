
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),

    path('category/<str:category_name>/',
         views.books_by_category,
         name='books_by_category'),

    path('<int:book_id>/',
         views.book_detail,
         name='book_detail'),
]
