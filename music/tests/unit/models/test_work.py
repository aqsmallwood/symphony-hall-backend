from unittest.mock import MagicMock, patch
import pytest

from music.models import Work
from people.models import Composer


def test_work_has_necessary_fields():
    work = Work()
    work.id = 1

    assert True == hasattr(work, 'id')
    assert True == hasattr(work, 'name')
    assert True == hasattr(work, 'composers')


def test_work_has_meaningful_string_representation():
    work = Work()
    work.id = 1
    work.name = 'Moonlight Sonata'

    expected_string_representation = 'Moonlight Sonata'
    assert expected_string_representation == str(work)
