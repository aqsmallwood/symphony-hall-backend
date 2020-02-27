
from django.urls import reverse


def test_index_view(client):
    url = reverse('index')

    response = client.get(url)

    assert 200 == response.status_code
