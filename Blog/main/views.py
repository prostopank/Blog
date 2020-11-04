from django.shortcuts import render
from .models import User

def index(request):
    users = User.objects.all()
    return render(request, 'main/index.html', {'title':'All users', 'users': users})

def sign_in(reques):
    
    return render(reques, 'main/signin.html')

