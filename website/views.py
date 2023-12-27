from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# Home page
def index(request):
    return render(request, 'website/index.html')

def lga_score(request):
    return render(request, 'website/lga_score.html')

@login_required(login_url='/login')
def upload_score(request):
    return render(request, 'website/upload_score.html')

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'website/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'website/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
