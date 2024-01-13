from ..forms import CreateUserForm
from ..models import CustomUser
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