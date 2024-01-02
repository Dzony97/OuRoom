from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

#Django user registration form. Inherits from the built-in UserCreationForm form that provides the functionality to handle the user creation process.
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] # List of fields to be included in the form.