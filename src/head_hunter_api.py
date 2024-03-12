import json
import os

import requests

from src.api_abstract import APIAbstract


class HeadHunterAPI(APIAbstract):
    """
    Класс, который получает информацию о вакансиях hh.ru
    """
    API_KEY = os.getenv('API_HH')

    def getting_vacancies(self, text: str, per_page: int):
        """
        :param per_page: количество вакансий
        :param text: информация для поиска вакансий на hh.ru
        :return: список вакансий с hh.ru
        """

        params = {'area': 113,
                  'text': text,
                  'per_page': per_page}
        __url = "https://api.hh.ru/vacancies"
        response = requests.get(__url, params=params,
                                headers={'apikey': self.API_KEY})
        if response.status_code == 200:
            response_data = json.loads(response.text)
            return response_data['items']
        raise ConnectionError
