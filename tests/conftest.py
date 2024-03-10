import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy1():
    return Vacancy("Специалист по прямым продажам",
                   "https://api.hh.ru/vacancies/92644069?host=hh.ru",
                   3000,
                   15000,
                   "Россия",
                   "2024-02-19T09:38:06+0300")


@pytest.fixture
def vacancy2():
    return Vacancy("Специалист по прямым продажам",
                   "https://api.hh.ru/vacancies/92644069?host=hh.ru",
                   None,
                   None,
                   "Россия",
                   "2024-02-19T09:38:06+0300")

