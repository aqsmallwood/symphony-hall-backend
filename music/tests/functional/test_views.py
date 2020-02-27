import pytest
from django.urls import reverse

from music.models import Work
from people.models import Composer


@pytest.mark.django_db
def test_get_works_when_no_works_then_return_empty_list(client):
    url = reverse('work-list')

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_get_works_when_works_exist_then_return_empty_list(client):
    test_composer = Composer.objects.create(
        given_name='Maurice', family_name='Ravel')

    test_work = Work.objects.create(name='Bolero')
    test_work.composers.add(test_composer)
    url = reverse('work-list')

    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1
    work = response.data[0]
    assert work['id'] == test_work.id
    assert work['name'] == test_work.name
    assert work['composers'][0]['id'] == test_composer.id
