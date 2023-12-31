from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

# User login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Daisies:homepage')
        else:
            return render(request, 'user_auth/login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'user_auth/login.html')
    
# User registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_auth:user_login')
        else:
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})

#user profile view
@login_required
def profile(request):
    user = request.user
    return render(request, 'user_auth/profile.html')

#Logout view
def user_logout(request):
    logout(request)
    return redirect('user_auth:user_login')


