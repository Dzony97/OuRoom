from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from .models import CustomUser

from django.contrib.auth.models import auth
from django.contrib import messages

def sign_up(request):

    form = CreateUserForm()

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        form = CreateUserForm(request.POST)

        if password1 != password2:
            messages.warning(request, "Podane hasła różnią się od siebie.")
        elif CustomUser.objects.filter(username=username).exists():
            messages.info(request, 'Nazwa użytkwnika jest już zajęta.')
        elif CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'Podany email jest już zajęty.')

        if form.is_valid():
            messages.success(request, 'Twoje konto zostało utworzone. Możesz się zalogować.')
            form.save() # If the form is valid, saving the user.
            return redirect('log_in')
        else:
            for field in form.errors:
                for error in form[field].errors:
                    messages.error(request, error)



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






