import pytest

from config import TEST_VACANCIES_FILE
from src.vacancy import Vacancy


def test_vacancy1(vacancy1):
    assert vacancy1.area == 'Россия'


def test_vacancy2(vacancy2):
    assert vacancy2.salary_to == 0
    assert vacancy2.salary_from == 0


def test_vacancy3(vacancy1):
    assert vacancy1 <= 20000
    assert vacancy1 >= 300
    with pytest.raises(TypeError):
        vacancy1 <= 'vacancy1'



def test_cast_to_object_list():
    assert Vacancy.cast_to_object_list(TEST_VACANCIES_FILE)[0].name == 'Удаленный диспетчер чатов (в Яндекс)'
