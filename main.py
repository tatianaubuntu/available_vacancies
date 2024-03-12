from src.filter_functions import (get_vacancies_by_salary, sort_vacancies,
                                  get_top_vacancies, print_vacancies)
from src.head_hunter_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def user_interaction():
    """
    Функция по работе с пользователем
    """
    search_query = input("""Добро пожаловать на платформу 'HeadHunter'
Пожалуйста, введите поисковый запрос: """)
    per_page = int(input("Количество вакансий для сохранения: "))
    hh_api = HeadHunterAPI()
    vacancies = hh_api.getting_vacancies(search_query, per_page)
    json_saver = JSONSaver()
    json_saver.save_vacancies(vacancies)
    json_vacancies = json_saver.open_vacancies()
    vacancies_list = Vacancy.cast_to_object_list(json_vacancies)
    json_vacancies.close()
    salary_range = input("Введите диапазон зарплат через пробел: ").split()
    ranged_vacancies = get_vacancies_by_salary(vacancies_list, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_n = input("Введите количество вакансий для вывода в топ N: ")
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
