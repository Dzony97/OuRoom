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

            if user is not None: # If user is in DB login
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

    show_settings = False  # Flag for change profile/settings

    if request.method == "POST":

        u_form = UserUpdateForm(request.POST, instance=request.user) # operating on an existing model instance
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # operating on an model profile
        ch_form = SetPasswordForm(request.user, request.POST)
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if request.POST['action'] == 'update_profile': # action update_profile_data

            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Twoje konto zostało zaktualizowane!')
                return redirect('profile')

        if request.POST['action'] == 'update_password': # action change password

            if ch_form.is_valid():
                ch_form.save()
                messages.success(request, f'Twoje hasło zostało zmienione!')
                update_session_auth_hash(request, request.user) # prevents logging out
                return redirect('profile')
            elif new_password1 != new_password2:
                messages.error(request, "Podane hasła różnią się od siebie!")
                show_settings = True

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        ch_form = SetPasswordForm(request.user)

    user_profile, created = Profile.objects.get_or_create(user=request.user) # Created or download user profile

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': user_profile,
        'ch_form': ch_form,
        'show_settings': show_settings
    }

    return render(request, 'rooms/profile.html', context)

def password_reset(request):
    return render(request, 'accounts/password_reset.html')



