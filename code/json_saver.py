import json

from code.file_abstract import FileAbstract
from config import VACANCIES_FILE


class JSONSaver(FileAbstract):
    """
    Класс для работы с JSON-файлом вакансий
    """

    def save_vacancies(self, vacancies: list):
        """
        :param vacancies: список вакансий с сайта
        Метод сохраняет данные в JSON-файл
        """
        with open(VACANCIES_FILE, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f)
            print('Информация сохранена')

    def add_vacancy(self, vacancy: dict):
        """
        :param vacancy: новая вакансия
        Метод добавляет вакансию в JSON-файл
        """
        with open(VACANCIES_FILE) as json_file:
            data_list = json.load(json_file)
        data_list.append(vacancy)
        with open(VACANCIES_FILE, "w") as json_file:
            json.dump(data_list, json_file)

    def del_vacancy(self, vacancy: dict):
        """
        :param vacancy: вакансия
        Метод удаляет вакансию из JSON-файла
        """
        with open(VACANCIES_FILE, "r+") as json_file:
            data_list = json.load(json_file)
            try:
                if vacancy in data_list:
                    del vacancy
            except ValueError:
                print('Вакансия отсутствует в файле')
