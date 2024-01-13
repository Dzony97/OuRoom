from ..forms import CreateUserForm
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