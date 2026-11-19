
from django.http import HttpResponse
from django.shortcuts import render

BOOKS = [
    {
        'id' : 1, 
        'title' : 'clean code', 
        'author' : 'Robert C. Martin',
        'category' : 'programming',
        'price' : 2450.5,
        'copy' : 4
    },
    {
        'id' : 2, 
        'title' : 'the pragmatic programmer ', 
        'author' : 'Andrew Hunt',
        'category' : 'programming',
        'price' : 2800,
        'copy' : 0
    },
    {
        'id' : 3, 
        'title' : 'database system concepts', 
        'author' : 'Abraham Silberschatz',
        'category' : 'databases',
        'price' : 3150.75,
        'copy' : 2
    },
    {
        'id' : 4, 
        'title' : 'computer networking', 
        'author' : ' James Kurose',
        'category' : 'networks',
        'price' : 2999,
        'copy' : 1
    },
    {
        'id' : 5, 
        'title' : 'operating system concepts', 
        'author' : 'Abraham Silberschatz',
        'category' : 'systems',
        'price' : 3300,
        'copy' : 0
    },
    {
        'id' : 6, 
        'title' : 'two scoops of django', 
        'author' : 'Daniel Greenfeld',
        'category' : 'programming',
        'price' : 1890.25,
        'copy' : 3
    },
]

def book_list(request):

    context = {
        'books': BOOKS,
       'page_title': 'Books',
    }

    return render(
        request,
        'books/book_list.html',
        context
    )


def book_detail(request, book_id):
    book = next((b for b in BOOKS if b['id'] == book_id), None)
    if book is None:
        from django.http import Http404
        raise Http404("Book not found")
    return render(request, 'books/book_detail.html', {'book': book})


def books_by_category(request, category_name):
    filtered = [b for b in BOOKS if b['category'] == category_name]
    context = {
        'books': filtered,
        'page_title': f'Books in category: {category_name}',
        'category_name': category_name,
    }
    return render(request, 'books/book_list.html', context)


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