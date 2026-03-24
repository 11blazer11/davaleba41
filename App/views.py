from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#authenticate, login, logout gamoyeneba chatgpt davixmare
#kide argon2 maq gamoyenebuli

def register_view(request):
    if request.method == 'POST':
        base_username = request.POST.get('username')
        password = request.POST.get('password')

        username = base_username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user:
            login(request, user)
            return redirect('main') 
        else:
            messages.error(request, "ver shexvedi")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def main_view(request):
    return render(request, 'main_page.html')
