class Vacancy:
    """
    Класс для работы с вакансией
    """
    def __init__(self, name: str, url: str, salary: dict, area: str, published_at: str):
        """
        :param name: название вакансии
        :param url: ссылка на вакансию
        :param salary: предлагаемая зарплата
        :param area: описании вакансии
        :published_at: дата публикации
        """
        self.name = name
        self.url = url
        try:
            if not salary:
                raise TypeError
        except TypeError:
            self.__salary = 0
        self.__salary = salary
        self.area = area
        self.published_at = published_at

    @classmethod
    def new_vacancy(cls, vacancy: dict):
        """
        :param vacancy: словарь с новой вакансией
        :return: объект класса Vacancy
        """
        return cls(**vacancy)

    def __le__(self, other):
        return self.__salary <= other.salary

    def __ge__(self, other):
        return self.__salary >= other.salary


