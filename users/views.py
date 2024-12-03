from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm,SignInForm

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        print(form)
        print('POST data:', request.POST)
        if True:
            user = form.get_user()
            print(user)
            login(request, user)
            messages.success(request, f"Chào mừng, {user.username}!")
            return redirect('store')
        else:
            print(form.errors)
            messages.error(request, "Form invalid")
    else:
        form = SignInForm()
    return render(request, 'registration/signin.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        print('POST data:', request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)  
            return redirect('store') 
        else:                           
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
