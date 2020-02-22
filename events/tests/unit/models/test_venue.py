from events.models import Venue


def test_venue_has_necessary_fields():
    venue = Venue()

    assert True == hasattr(venue, 'id')
    assert True == hasattr(venue, 'name')

def test_venue_has_meaningful_string_representation():
    test_venue_name = 'Sydney Opera House'
    
    venue = Venue(name=test_venue_name)

    assert test_venue_name == str(venue)
