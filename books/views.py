
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


def book_issue(request, book_id, days):
    if days < 14:
        return HttpResponse(f"Issuing book with ID: {book_id} for {days} days.")
    else:
        remaining_days = days - 14
        fine = remaining_days * 20 
        return HttpResponse(f"Book with ID: {book_id} issued for {days} days. Fine: ${fine}")

def top_books(request):
    return HttpResponse("""
        <h1>Top 5 Books</h1>
        <ol>
            <li>Atomic Habits</li>
            <li>Clean Code</li>
            <li>Deep Work</li>
            <li>Rich Dad Poor Dad</li>
            <li>The Alchemist</li>
        </ol>
    """)