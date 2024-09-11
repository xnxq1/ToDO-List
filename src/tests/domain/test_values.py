from src.domain.values.base import BaseDomainException
from src.domain.values.tasks import Title, TooLongTitleException


def test_title():
    title = Title('test')
    assert title.value == 'test'

    try:
        title = Title('a' * 300)
    except BaseDomainException as e:
        assert isinstance(e, TooLongTitleException)