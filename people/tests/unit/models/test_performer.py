from people.models import Performer


def test_performer_has_necessary_fields():
    performer = Performer()

    assert True == hasattr(performer, 'id')
    assert True == hasattr(performer, 'name')


def test_performer_has_meaningful_string_representation():
    test_performer_name = 'Fiddling Fiddler'
    performer = Performer(name=test_performer_name)
    assert test_performer_name == str(performer)
