from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def sign_up(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST) # If yes, creating a CreateUserForm based on the data from the request.

        if form.is_valid():
            form.save() # If the form is valid, saving the user.
            return redirect('log_in')

    context = {'registerform': form} # Passing the form to the template for rendering.

    return render(request, 'accounts/signup.html', context=context)

def log_in(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            #Retrieving username and password from POST data
            username = request.POST.get('username')
            password = request.POST.get('password')

            #User authentication using the authenticate function
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('main_room')

    context = {'loginform': form}

    return render(request, 'accounts/login.html', context=context)

def logout(request):

    auth.logout(request)
    return redirect('log_in')






