from ..forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm, SetPasswordForm
from ..models import CustomUser, Profile
import pytest

@pytest.mark.django_db
def test_account_register_form_success():
    # Arrange
    form = CreateUserForm({"username": "Patryk",
                           "email": "patrykpalonka@wp.pl",
                           "first_name": "Patryk",
                           "last_name": "Palonka",
                           "password1": "haslohaslo",
                           "password2": "haslohaslo",
                           })

    # Action
    result = form.is_valid()

    # Assert
    assert result is True

@pytest.mark.django_db
def test_account_register_form_fail():
    # Arrange
    form = CreateUserForm({"username": "Patryk",
                           "email": "patrykpalonka@wp.pl",
                           "first_name": "Patryk",
                           "last_name": "Palonka",
                           "password1": "haslohaslo",
                           "password2": "haslohaso",
                           })

    # Action
    result = form.is_valid()

    # Assert
    assert result is False

@pytest.mark.django_db
def test_account_register_form_invalid_duplicate_email():
    # Arrange
    CustomUser.objects.create(email="patrykpalonka@wp.pl")

    form = CreateUserForm({"username": "Patryk",
                           "email": "patrykpalonka@wp.pl",
                           "first_name": "Patryk",
                           "last_name": "Palonka",
                           "password1": "haslohaslo",
                           "password2": "haslohaslo",
                           })

    # Action
    result = form.is_valid()

    # Assert
    assert result is False
    assert form.errors["email"][0] == "User with this Email already exists."

@pytest.mark.django_db
def test_account_register_form_invalid_duplicate_username():
    # Arrange
    CustomUser.objects.create(username="TestUser")

    form = CreateUserForm({"username": "TestUser",
                           "email": "patrykpalonka@wp.pl",
                           "first_name": "Patryk",
                           "last_name": "Palonka",
                           "password1": "haslohaslo",
                           "password2": "haslohaslo",
                           })

    # Action
    result = form.is_valid()

    # Assert
    assert result is False
    assert form.errors["username"][0] == "A user with that username already exists."

@pytest.mark.django_db
def test_user_update_form_success():
    # Arrange
    user = CustomUser.objects.create_user(username='testowy', password='12335', last_name='testname', first_name='firsttest')

    form_data = {"last_name": "Nazwisko", "first_name": "Imię"}

    form = UserUpdateForm(data=form_data, instance=user)

    #Action
    result = form.is_valid()
    if result:
        form.save()
        user.refresh_from_db()

    #Assert
    assert result is True
    assert user.last_name == "Nazwisko"
    assert user.first_name == "Imię"

@pytest.mark.django_db
def test_user_update_form_fail():
    #Arrange
    form = UserUpdateForm({"last_name": "",
                           "first_name": "Imię",})

    #Action
    result = form.is_valid()

    #Assert
    assert result is False

@pytest.mark.django_db
def test_profile_update_form_fail():
    # Arrange
    user = CustomUser.objects.create_user(username='testuser', password='12345')
    profile = Profile.objects.create(user=user, location='New Location', birth_date='2000-01-01')

    form_data = {
        "location": "Krasnystaw",
        "birth_date": "2023-13-13",
    }
    form = ProfileUpdateForm(data=form_data, instance=profile)

    # Action
    result = form.is_valid()

    # Assert
    assert result is False

@pytest.mark.django_db
def test_profile_update_form_success():
    # Arrange
    user = CustomUser.objects.create_user(username='testuser', password='12345')
    profile = Profile.objects.create(user=user, location='New Location', birth_date='2000-01-01')

    form_data = {
        "location": "Krasnystaw",
        "birth_date": "2023-12-12",
    }
    form = ProfileUpdateForm(data=form_data, instance=profile)

    # Action
    result = form.is_valid()
    if result:
        form.save()
        profile.refresh_from_db()

    # Assert
    assert result is True
    assert profile.location == "Krasnystaw"
    assert profile.birth_date.strftime('%Y-%m-%d') == "2023-12-12"

@pytest.mark.django_db
def test_change_password_success():

    #Arrange
    user = CustomUser.objects.create_user(username='testuser', email='user@test.com', password='password')

    form_data = {'new_password1': 'new_password', 'new_password2': 'new_password'}

    form = SetPasswordForm(user, form_data)

    #Action
    result = form.is_valid()
    if result:
        form.save()
        user.refresh_from_db()

    #Assert
    assert result is True

@pytest.mark.django_db
def test_change_password_fail():

    # Arrange
    user = CustomUser.objects.create_user(username='testuser', email='user@test.com', password='password')

    form_data = {'new_password1': '1', 'new_password2': '1'}

    form = SetPasswordForm(user, form_data)

    #Action
    result = form.is_valid()
    if result:
        form.save()
        user.refresh_from_db()

    #Assert
    assert result is False


