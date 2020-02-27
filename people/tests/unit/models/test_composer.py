from people.models import Composer


def test_composer_has_necessary_fields():
    composer = Composer()

    assert True == hasattr(composer, 'id')
    assert True == hasattr(composer, 'given_name')
    assert True == hasattr(composer, 'family_name')


def test_composer_has_meaningful_string_representation():
    test_given_name = 'Pyotr Illych'
    test_family_name = 'Tchaikovsky'

    composer = Composer(given_name=test_given_name,
                        family_name=test_family_name)

    expected_string_representation = 'Tchaikovsky, Pyotr Illych'
    assert expected_string_representation == str(composer)


def test_composer_has_full_name_property():
    test_given_name = 'Pyotr Illych'
    test_family_name = 'Tchaikovsky'

    composer = Composer(given_name=test_given_name,
                        family_name=test_family_name)

    expected_full_name = 'Pyotr Illych Tchaikovsky'
    assert expected_full_name == composer.full_name
