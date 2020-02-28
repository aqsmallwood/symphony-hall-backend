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


@pytest.mark.django_db
def test_post_heard_work_when_work_does_not_exist_then_return_404(client):
    url = reverse('work-heard', kwargs={'pk': 100})

    response = client.post(url)

    assert response.status_code == 404


@pytest.mark.skip
@pytest.mark.django_db
def test_post_heard_work_when_work_exists_then_return_201(client):
    test_composer = Composer.objects.create(
        given_name='Franz', family_name='Schubert')

    test_work = Work.objects.create(name='Arpeggione Sonata')
    test_work.composers.add(test_composer)

    url = reverse('work-heard', kwargs={'pk': test_work.id})

    response = client.post(url)

    assert response.status_code == 201


@pytest.mark.django_db
def test_post_seen_work_when_work_does_not_exist_then_return_404(client):
    url = reverse('work-seen', kwargs={'pk': 100})

    response = client.post(url)

    assert response.status_code == 404


@pytest.mark.skip
@pytest.mark.django_db
def test_post_seen_work_when_work_exists_then_return_201(client):
    test_composer = Composer.objects.create(
        given_name='Franz', family_name='Schubert')

    test_work = Work.objects.create(name='Arpeggione Sonata')
    test_work.composers.add(test_composer)

    url = reverse('work-seen', kwargs={'pk': test_work.id})

    response = client.post(url)

    assert response.status_code == 201
