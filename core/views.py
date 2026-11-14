from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <h1>Welcome to the Library Management System</h1>
        <a href="/books/">Book List</a>
        <br>
        <a href="/members/">Member List</a>
    """)