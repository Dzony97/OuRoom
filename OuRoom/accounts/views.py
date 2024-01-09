from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib import messages

def sign_up(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST) # If yes, creating a CreateUserForm based on the data from the request.

        if form.is_valid():
            messages.success(request, 'Twoje konto zostało utworzone. Możesz się zalogować.')
            form.save() # If the form is valid, saving the user.

            username = form.cleaned_data.get('username')

            return redirect('log_in')

    context = {'registerform': form} # Passing the form to the template for rendering.

    return render(request, 'accounts/signup.html', context=context)

def log_in(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user is not None:
                auth.login(request, user)
                return redirect('main_room')

        else:
            messages.error(request, 'Niepoprawny login lub hasło.')

    context = {'loginform': form}

    return render(request, 'accounts/login.html', context=context)

def logout(request):

    auth.logout(request)
    return render(request, 'accounts/logout.html')

def welcome(request):
    return render(request, 'accounts/welcome.html')






