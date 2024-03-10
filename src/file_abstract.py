from abc import ABC, abstractmethod


class FileAbstract(ABC):
    """
    Абстрактный класс работы с файлами вакансий
    """
    @abstractmethod
    def save_vacancies(self, vacancies: list):
        """
        :param vacancies: список вакансий с сайта
        Сохраняет информацию о вакансиях в файл
        """
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: dict):
        """
        :param vacancy: новая вакансия
        Метод добавляет вакансию в файл
        """
        pass

    @abstractmethod
    def del_vacancy(self, vacancy: dict):
        """
        :param vacancy: вакансия
        Метод удаляет вакансию из файла
        """
        pass

