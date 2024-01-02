from django.shortcuts import render, redirect
from . forms import CreateUserForm

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
    return render(request, 'accounts/login.html')


