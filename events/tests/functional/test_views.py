from django.urls import reverse

import pytest
from datetime import date

from events.models import Venue, Performance
from music.models import Work
from people.models import Composer


@pytest.mark.django_db
def test_get_venues_when_no_venues_then_return_empty_list(client):
    url = reverse('venue-list')

    response = client.get(url)

    assert response.data == []


@pytest.mark.django_db
def test_get_venues_when_venues_exist_then_return_list_of_venue_data(client):
    url = reverse('venue-list')

    test_venue_names = ['Ham Hall', 'Anthony Zuiker Theater']
    for test_venue in test_venue_names:
        Venue.objects.create(name=test_venue)

    response = client.get(url)
    assert response.status_code == 200
    data = response.data
    assert len(data) == len(test_venue_names)
    venue_names = [venue['name'] for venue in data]

    for test_venue_name in test_venue_names:
        assert test_venue_name in venue_names


@pytest.mark.django_db
def test_get_venue_when_venue_exists_then_return_venue(client):
    v = Venue.objects.create(name='Ham Hall')
    url = reverse('venue-detail', kwargs={'pk': v.id})

    response = client.get(url)

    assert response.status_code == 200
    assert response.data['name'] == 'Ham Hall'


@pytest.mark.django_db
def test_get_venue_when_venue_does_not_exist_then_return_404(client):
    url = reverse('venue-detail', kwargs={'pk': 1})

    response = client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_get_performances_when_no_performances_then_return_empty_list(client):
    url = reverse('performance-list')

    response = client.get(url)

    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_get_performances_when_performances_exist_then_return_list_of_performance_data(client):
    test_composer = Composer.objects.create(
        given_name='Camille', family_name='Saint-Saëns')
    test_work = Work.objects.create(name='The Swan')
    test_work.save()
    test_work.composers.add(test_composer)
    test_venue = Venue.objects.create(name='test venue')
    test_performance_date = date(2000, 1, 1)

    performance = Performance()
    performance.performed_at = test_performance_date
    performance.venue = test_venue
    performance.work = test_work
    performance.save()

    url = reverse('performance-list')

    response = client.get(url)

    assert response.status_code == 200
    returned_performances = response.data
    assert len(returned_performances) == 1
    assert returned_performances[0]['work']['id'] == test_work.id
    assert returned_performances[0]['performed_at'] == test_performance_date.isoformat(
    )
