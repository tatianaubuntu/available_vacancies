from abc import ABC, abstractmethod


class APIAbstract(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def getting_vacancies(self, text: str):
        """
        :param text: информация для поиска вакансий
        :return: исписок вакансий
        """
        pass
