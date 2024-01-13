from ..forms import CreateUserForm
import pytest

@pytest.mark.django_db
def test_account_register_form_success():
    # Arrange
    form = CreateUserForm({"username": "TestUser",
                           "email": "testuser@wp.pl",
                           "first_name": "Test",
                           "last_name": "User",
                           "password1": "inferno123",
                           "password2": "inferno123",
                           })

    # Action
    result = form.is_valid()

    if not result:
        print(form.errors)

    # Assert
    assert result is True