import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_create_user_when_valid_data_then_user_created(client):
    url = reverse('user-list')

    signup_data = {
        'username': 'new_user',
        'password1': 'SomethingForTheRep0',
        'password2': 'SomethingForTheRep0',
    }
    response = client.post(url, signup_data)

    assert response.status_code == 201


@pytest.mark.django_db
def test_create_user_when_username_exists_then_user_not_created(client):
    user = User.objects.create_user('existing_user')

    url = reverse('user-list')

    signup_data = {
        'username': 'existing_user',
        'password1': 'SomethingForTheRep0',
        'password2': 'SomethingForTheRep0',
    }
    response = client.post(url, signup_data)

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_user_when_username_exists_then_user_not_created(client):
    url = reverse('user-list')

    signup_data = {
        'username': 'new_user',
        'password1': 'SomethingForTheRep0',
        'password2': 'SomethingForTheRep',
    }
    response = client.post(url, signup_data)

    assert response.status_code == 400
