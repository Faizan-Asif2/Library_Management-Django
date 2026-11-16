from django.shortcuts import render
from django.http import Http404


MEMBERS = [
    {
        'id': 1,
        'name': 'Hamza Tariq',
        'membership': 'student',
        'book_issued': 1
    },
    {
        'id': 2,
        'name': 'Fatima Noor',
        'membership': 'faculty',
        'book_issued': 3
    },
    {
        'id': 3,
        'name': 'Usman Ali',
        'membership': 'student',
        'book_issued': 0
    },
    {
        'id': 4,
        'name': 'Zainab Hussain',
        'membership': 'student',
        'book_issued': 4
    },
]




def member_list(request):

    context = {
        'members': MEMBERS,
        'page_title': 'Members',
    }

    return render(
        request,
        'members/member_list.html',
        context
    )

def member_detail(request, member_id):
    return HttpResponse(f"<h1>Member id # {member_id}</h1>")

def member_info(request):
    method = request.method
    full_path = request.get_full_path()
    name = request.GET.get('name', 'Guest')

    return HttpResponse(f"""
        <h1>Request Information</h1>
        <p>HTTP Method: {method}</p>
        <p>Full Path: {full_path}</p>
        <p>Name: {name}</p>
    """)