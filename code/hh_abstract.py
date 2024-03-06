from abc import ABC, abstractmethod


class HhAbstract(ABC):
    """
    Абстрактный класс вакансий hh.ru
    """

    @abstractmethod
    def getting_vacancies(self):
        pass
