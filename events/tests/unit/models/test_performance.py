from datetime import date

from music.models import Work
from events.models import Performance


def test_performance_has_necessary_fields():
    performance = Performance()
    # Required before access to related fields ('performers') is allowed
    performance.id = 1

    assert True == hasattr(performance, 'id')
    assert True == hasattr(performance, 'performed_at')
    assert True == hasattr(performance, 'performers')


def test_performance_has_meaningful_string_representation():
    test_work_name = 'Symphony 1'
    test_work = Work()
    test_work.name = test_work_name

    test_performance_date = date(2020, 1, 1)
    performance = Performance()
    performance.performed_at = test_performance_date
    performance.work = test_work

    expected_performance_name = f'{test_performance_date} {test_work_name}'

    assert expected_performance_name == str(performance)
