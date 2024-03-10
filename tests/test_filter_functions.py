from src.filter_functions import print_vacancies


def test_get_vacancies_by_salary1(vacancies_by_salary1):
    assert vacancies_by_salary1[0].name == 'Удаленный диспетчер чатов (в Яндекс)'


def test_get_vacancies_by_salary2(vacancies_by_salary2):
    assert len(vacancies_by_salary2) == 1


def test_sort_vacancies(ranged_vacancies):
    assert ranged_vacancies[0].name == 'Удаленный специалист службы поддержки (в Яндекс)'


def test_get_top_vacancies1(top_vacancies1):
    assert len(top_vacancies1) == 2


def test_get_top_vacancies2(top_vacancies2):
    assert len(top_vacancies2) == 2


