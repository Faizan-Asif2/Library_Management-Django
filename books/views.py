
from django.http import HttpResponse


def book_list(request):
    return HttpResponse("""
        <h1>Library Book Collection</h1>
        <p>Welcome to our library! Explore our collection of books.</p>
    """)


def book_detail(request, book_id):
    return HttpResponse(f"Book ID: {book_id}")


def books_by_category(request, category_name):
    return HttpResponse(f"Books in category: {category_name}")
