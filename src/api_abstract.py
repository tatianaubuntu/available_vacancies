from abc import ABC, abstractmethod


class APIAbstract(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def getting_vacancies(self, text: str, per_page: int):
        """
        :param per_page: количество вакансий
        :param text: информация для поиска вакансий
        :return: список вакансий
        """
        pass
