import json


class Vacancy:
    """
    Класс для работы с вакансией
    """
    __slots__ = ('name', 'url', '__salary_from',
                 '__salary_to', 'area', 'published_at')

    def __init__(self,
                 name: str,
                 url: str,
                 salary_from: int,
                 salary_to: int,
                 area: str,
                 published_at: str):
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
        try:
            self.__salary_from = salary_from
            if not salary_from:
                raise TypeError
        except TypeError:
            self.__salary_from = 0
        try:
            self.__salary_to = salary_to
            if not salary_to:
                raise TypeError
        except TypeError:
            self.__salary_to = 0
        self.area = area
        self.published_at = published_at

    @classmethod
    def cast_to_object_list(cls, vacancies_json: json):
        """
        :param vacancies_json: информация о вакансиях в формате JSON
        :return: список объектов вакансий
        """
        data_list = json.load(vacancies_json)
        vacancies_list = []
        for vacancy in data_list:
            try:
                (name, url, salary_from,
                 salary_to, area, published_at) = (vacancy['name'],
                                                   vacancy['url'],
                                                   vacancy['salary']['from'],
                                                   vacancy['salary']['to'],
                                                   vacancy['area']['name'],
                                                   vacancy['published_at'])
            except TypeError:
                (name, url, salary_from,
                 salary_to, area, published_at) = (vacancy['name'],
                                                   vacancy['url'],
                                                   0,
                                                   0,
                                                   vacancy['area']['name'],
                                                   vacancy['published_at'])
            vacancies_list.append(cls(name, url, salary_from,
                                      salary_to, area, published_at))
        return vacancies_list

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @staticmethod
    def __type_error(salary: int):
        if not isinstance(salary, int):
            raise TypeError
        return salary

    def __le__(self, salary_to: int):
        """
        :param salary_to: зарплата, предлагаемая пользователем до
        :return: True, если self.__salary_to <= salary_to
        """
        return self.__salary_to <= self.__type_error(salary_to)

    def __ge__(self, salary_from: int):
        """
        :param salary_from: зарплата, предлагаемая пользователем от
        :return: True, если self.__salary_from >= salary_from
        """
        return self.__salary_from >= self.__type_error(salary_from)
