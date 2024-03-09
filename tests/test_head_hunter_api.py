import pytest

from code.head_hunter_api import HeadHunterAPI


@pytest.fixture
def head_hunter_api():
    return HeadHunterAPI()


def test_getting_vacancies(head_hunter_api):
    assert head_hunter_api.getting_vacancies('Python')[0]['name'] == 'Стажер-разработчик Python'
    # with pytest.raises(ConnectionError):
    #     head_hunter_api.getting_vacancies('Python')
