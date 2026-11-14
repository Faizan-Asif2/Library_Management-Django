from django.http import HttpResponse

def member_list(request):
    return HttpResponse("<h1>Member FeeZi Zanii</h1>")

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