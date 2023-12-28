from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm, PollingForm
from django.contrib.auth.decorators import login_required
from .models import State, LGA, Ward, PollingUnit


# Create your views here.
# Home page
def index(request):

    form = PollingForm()
    if request.method == 'POST':
        form = PollingForm(request.POST)
        if form.is_valid():
            selected_state = form.cleaned_data['state']
            selected_lga = form.cleaned_data['lga']
            selected_ward = form.cleaned_data['ward']
            selected_polling_unit = form.cleaned_data['polling_unit']
            # ... use these values for filtering
            print(selected_state)
            print(selected_lga)
            print(selected_ward)
            print(selected_polling_unit)
                   
    return render(request, 'website/index.html', {'form':form})

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
