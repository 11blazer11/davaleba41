from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#authenticate, login, logout gamoyeneba chatgpt davixmare
#kide argon2 maq gamoyenebuli

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')
        
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})




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
