from people.models import Performer


def test_performer_has_necessary_fields():
    performer = Performer()

    assert True == hasattr(performer, 'name')
