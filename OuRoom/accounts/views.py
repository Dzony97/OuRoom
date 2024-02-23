from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, ProfileUpdateForm, UserUpdateForm, SetPasswordForm
from .models import CustomUser, Profile

from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
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

@login_required
def profile_view(request):

    if request.method == "POST":

        u_form = UserUpdateForm(request.POST, instance=request.user) # instance mówi formularzowi, że ma on operować na istniejącej instancji modelu
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # instance mowi formularzowi ze ma operować na modelu profile
        ch_form = SetPasswordForm(request.user, request.POST)

        if ch_form.is_valid():
            ch_form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, f'Twoje hasło zostało zmienione!')
            return redirect('profile')

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Twoje konto zostało zaktualizowane!')
            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        ch_form = SetPasswordForm(request.user)

    user_profile, created = Profile.objects.get_or_create(user=request.user) #  # Created or download user profile

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': user_profile,
        'ch_form': ch_form
    }


    return render(request, 'rooms/profile.html', context)




