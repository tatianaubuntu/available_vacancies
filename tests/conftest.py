import pytest

from config import TEST_VACANCIES_FILE
from src.filter_functions import (get_vacancies_by_salary,
                                  sort_vacancies, get_top_vacancies)
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


@pytest.fixture
def vacancies():
    with open(TEST_VACANCIES_FILE) as f:
        return Vacancy.cast_to_object_list(f)


@pytest.fixture
def vacancies_by_salary1(vacancies):
    return get_vacancies_by_salary(vacancies, [0])


@pytest.fixture
def vacancies_by_salary2(vacancies):
    return get_vacancies_by_salary(vacancies, [0, 40000])


@pytest.fixture
def ranged_vacancies(vacancies_by_salary1):
    return sort_vacancies(vacancies_by_salary1)


@pytest.fixture
def top_vacancies1(ranged_vacancies):
    return get_top_vacancies(ranged_vacancies, '5')


@pytest.fixture
def top_vacancies2(ranged_vacancies):
    return get_top_vacancies(ranged_vacancies, '')
