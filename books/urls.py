
from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='book_list'),

    path('category/<str:category_name>/',
         views.books_by_category,
         name='books_by_category'),

    path('<int:book_id>/',
         views.book_detail,
         name='book_detail'),
    path('issue/<int:book_id>/<int:days>/',
         views.book_issue,
         name='book_issue'),
    path('top-books/', views.top_books, name='top_books'),]
