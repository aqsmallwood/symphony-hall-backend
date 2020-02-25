import pytest

from django.urls import reverse

from people.models import Composer, Performer

@pytest.mark.django_db
def test_get_composers_when_no_composers_returns_empty_list(client):
    url = reverse('composer-list')

    response = client.get(url)

    assert response.data == []


@pytest.mark.django_db
def test_get_composers_when_composers_exist_then_return_list_of_composer_data(client):
    url = reverse('composer-list')
    
    test_composers = [('Modest', 'Mussorgsky'), ('Maurice', 'Ravel')]
    for test_composer in test_composers:
        Composer.objects.create(given_name=test_composer[0], family_name=test_composer[1])

    response = client.get(url)
    data = response.data
    assert len(data) == len(test_composers)
    given_names = [c['given_name'] for c in data]
    family_names = [c['family_name'] for c in data]
    
    for test_composer in test_composers:
        assert test_composer[0] in given_names
        assert test_composer[1] in family_names


@pytest.mark.django_db(transaction=True)
def test_get_composer_when_composer_does_not_exist_then_404(client):
    url = reverse('composer-detail', kwargs={'pk': 1})

    response = client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_get_composer_when_composer_exists_then_return_composer(client):
    c = Composer.objects.create(given_name='given', family_name='family')
    url = reverse('composer-detail', kwargs={'pk': c.id})

    response = client.get(url)

    assert response.status_code == 200
    assert response.data['given_name'] == 'given'
    assert response.data['family_name'] == 'family'


@pytest.mark.django_db
def test_get_performers_when_no_performers_returns_empty_list(client):
    url = reverse('performer-list')

    response = client.get(url)

    assert response.data == []

@pytest.mark.django_db
def test_get_performers_when_performers_exist_then_return_list_of_performer_data(client):
    url = reverse('performer-list')
    
    test_perfomers = ['Andy Smith', 'Bradley Taylor']
    for test_perfomer in test_perfomers:
        Performer.objects.create(name=test_perfomer)

    response = client.get(url)
    data = response.data
    assert len(data) == len(test_perfomers)
    names = [c['name'] for c in data]
    
    for test_perfomer in test_perfomers:
        assert test_perfomer in names

@pytest.mark.django_db
def test_get_performer_when_performer_does_not_exist_then_404(client):
    url = reverse('performer-detail', kwargs={'pk': 1})

    response = client.get(url)

    assert response.status_code == 404

@pytest.mark.django_db
def test_get_performer_when_performer_exists_then_return_performer(client):
    p = Performer.objects.create(name="Boston Pops")
    url = reverse('performer-detail', kwargs={'pk': p.id})

    response = client.get(url)

    assert response.status_code == 200
    assert response.data['name'] == 'Boston Pops'
