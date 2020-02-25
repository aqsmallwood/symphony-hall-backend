from django.urls import reverse

import pytest

from events.models import Venue, Performance


@pytest.mark.django_db
def test_get_venues_when_no_venues_returns_empty_list(client):
    url = reverse('venue-list')

    response = client.get(url)

    assert response.data == []


@pytest.mark.django_db
def test_get_venues_when_venues_exist_return_list_of_venue_data(client):
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
def test_get_performances_when_no_performances_returns_empty_list(client):
    url = reverse('performance-list')

    response = client.get(url)

    assert response.data == []
