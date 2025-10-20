from django.shortcuts import render, redirect
from .models import User

def index(request):
    if request.method == "POST":
        # Sign In form
        if 'signin' in request.POST:
            name = request.POST.get ('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            User.objects.create(name=name,email=email, password=password, form_type='signin')
            return redirect('success')

        # Login form
        elif 'login' in request.POST:
            name = request.POST.get('name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            User.objects.create(name=name, username=username, email=email, password=password, form_type='login')
            return redirect('success')

    return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')