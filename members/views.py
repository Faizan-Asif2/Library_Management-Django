from django.http import HttpResponse

def member_list(request):
    return HttpResponse("<h1>Member FeeZi Zanii</h1>")

def member_detail(request, member_id):
    return HttpResponse(f"<h1>Member id # {member_id}</h1>")