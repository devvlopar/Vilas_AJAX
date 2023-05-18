from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def index(request):
    a_l = User.objects.all()
    return render(request, 'index.html', {'all_u': a_l})


def add_data(request):
    User.objects.create(
        # POST ke andar jo key hai wo d1 ki keys hai
        first_name = request.POST['fname'],
        last_name = request.POST['lname'],
        email = request.POST['email']
    )
    all_users = list(User.objects.values()) # because JS mein jaa rha hai
    return JsonResponse({'all_u': all_users})
    
    


def del_data(request):
    row_id = request.GET['uid']
    u1 = User.objects.get(id = int(row_id))
    u1.delete()
    all_users = list(User.objects.values()) # because JS mein jaa rha hai
    return JsonResponse({'all_u': all_users})