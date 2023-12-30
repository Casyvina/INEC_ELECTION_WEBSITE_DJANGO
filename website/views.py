from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm, PollingForm
from django.contrib.auth.decorators import login_required
from .models import State, LGA, Ward, PollingUnit, AnnouncedPuResult
from django.http import HttpResponseBadRequest


# Create your views here.
# Home page
def index_(request):

    form = PollingForm()
    if request.method == 'POST':
        form = PollingForm(request.POST)
        if form.is_valid():
            selected_state = form.cleaned_data['state']
            selected_lga = form.cleaned_data['lga']
            selected_ward = form.cleaned_data['ward']
            selected_polling_unit = form.cleaned_data['polling_unit']
            # ... use these values for filtering
            results = AnnouncedPuResult.objects.filter(
                                                        state=selected_state,
                                                        lga=selected_lga,
                                                        ward=selected_ward,
                                                        polling_unit=selected_polling_unit
                                                        )
            print(results)

                   
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

def index(request):
    
    states = State.objects.all()
    context = {'states': states}
    return render(request, 'website/index.html', context)
    

def get_lgas_for_state(request):
    if request.method == 'GET':
        state_id = request.GET.get('state')
        if state_id:
            lgas = LGA.objects.filter(state=state_id)
            print(lgas)
            context = {'lgas': lgas}
            return render(request, 'website/partials/lga_options.html', context)
        else:
            return HttpResponseBadRequest('State ID is required')
        
def get_wards_for_lga(request):
    if request.method == 'GET':
        lga_id = request.GET.get('lga')
        if lga_id:
            wards = Ward.objects.filter(lga=lga_id)
            context = {'wards': wards}
            return render(request, 'website/partials/ward_options.html', context)
        else:
            return HttpResponseBadRequest('Lga ID is required')

def get_polling_units_for_ward(request):
    if request.method == 'GET':
        ward_id = request.GET.get('ward')
        if ward_id:
            print(ward_id)
            polling_units = PollingUnit.objects.filter(ward=ward_id)
            context = {'polling_units': polling_units}
            return render(request, 'website/partials/polling_unit_options.html', context)
        else:
            return HttpResponseBadRequest('Ward ID is required')
