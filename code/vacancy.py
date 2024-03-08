import json


class Vacancy:
    """
    Класс для работы с вакансией
    """

    def __init__(self, name: str, url: str, salary_from: int, salary_to: int, area: str, published_at: str):
        """
        :param name: название вакансии
        :param url: ссылка на вакансию
        :param salary_from: предлагаемая зарплата от
        :param salary_to: предлагаемая зарплата
        :param area: Регион
        :published_at: дата публикации
        """
        self.name = name
        self.url = url
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.area = area
        self.published_at = published_at

    @classmethod
    def cast_to_object_list(cls, vacancies_json: json):
        """
        :param vacancies_json: информация о вакансиях в формате JSON
        :return: список объектов вакансий
        """
        with open(vacancies_json, encoding='utf-8') as json_file:
            data_list = json.load(json_file)
            vacancies_list = []
            for vacancy in data_list:
                try:
                    name, url, salary_from, salary_to, area, published_at = (vacancy['name'],
                                                                             vacancy['url'],
                                                                             vacancy['salary']['from'],
                                                                             vacancy['salary']['to'],
                                                                             vacancy['area']['name'],
                                                                             vacancy['published_at'])
                except KeyError:
                    salary_from, salary_to = 0, 0
                vacancies_list.append(cls(name, url, salary_from, salary_to, area, published_at))
            return vacancies_list

    def __le__(self, salary_to: int):
        """
        :param salary_to: зарплата, предлагаемая пользователем до
        :return: True, если self.__salary_to <= salary_to
        """
        if not isinstance(salary_to, int):
            raise TypeError
        return self.__salary_to <= salary_to

    def __ge__(self, salary_from: int):
        """
        :param salary_from: зарплата, предлагаемая пользователем от
        :return: True, если self.__salary_from >= salary_from
        """
        if not isinstance(salary_from, int):
            raise TypeError
        return self.__salary_from >= salary_from
