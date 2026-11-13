from django.http import HttpResponse

def book_list(request):
    return HttpResponse("""
        <h1>Library Book Collection</h1>
        <p>Welcome to our library! Explore our collection of books.</p>
    """)

def book_detail(request, book_id):
    return HttpResponse(f"<h1>Book id {book_id}</h1>")