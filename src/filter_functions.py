from dateutil.parser import parse


def get_vacancies_by_salary(filtered_vacancies: list, salary_range: list):
    """
    :param filtered_vacancies: список отфильтрованных вакансий
    :param salary_range: диапазон зарплаты
    :return: список вакансий в соответствии с диапазоном зарплаты
    """
    vacancies_by_salary_list = []
    for vacancy in filtered_vacancies:
        try:
            if int(salary_range[0]) <= vacancy <= int(salary_range[1]):
                vacancies_by_salary_list.append(vacancy)
        except IndexError:
            vacancies_by_salary_list = filtered_vacancies
    return vacancies_by_salary_list


def sort_vacancies(ranged_vacancies: list):
    """
    :param ranged_vacancies: список вакансий с диапазоном зарплаты
    :return: отсортированный список вакансий по дате публикации
    """
    ranged_vacancies.sort(key=lambda vacancy: vacancy.published_at,
                          reverse=True)
    return ranged_vacancies


def get_top_vacancies(sorted_vacancies: list, top_n: str):
    """
    :param sorted_vacancies: отсортированный список вакансий по дате публикации
    :param top_n: количество вакансий
    :return: список вакансий top_n
    """
    try:
        return sorted_vacancies[:int(top_n)]
    except ValueError:
        return sorted_vacancies[:]


def print_vacancies(top_vacancies: list):
    """
    :param top_vacancies: список вакансий top_n
    Вывод вакансий на экран
    """
    for vacancy in top_vacancies:
        date = parse(vacancy.published_at)
        vacancy_print = (f"Наименование: {vacancy.name}, "
                         f"url: {vacancy.url}, "
                         f"зарплата от: {vacancy.salary_from}, "
                         f"зарплата до: {vacancy.salary_to}, "
                         f"регион: {vacancy.area}, "
                         f"дата публикации: {date:%d.%m.%Y} {date:%H:%M:%S}")
        print(vacancy_print)
