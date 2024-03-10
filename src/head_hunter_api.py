import json
import os

import requests

from src.api_abstract import APIAbstract


class HeadHunterAPI(APIAbstract):
    """
    Класс, который получает информацию о вакансиях hh.ru
    """
    API_KEY = os.getenv('API_HH')

    def getting_vacancies(self, text: str):
        """
        :param text: информация для поиска вакансий на hh.ru
        :return: список вакансий с hh.ru
        """

        params = {'area': 113,
                  'text': text}
        url = f'https://api.hh.ru/vacancies'
        response = requests.get(url, params=params, headers={'apikey': self.API_KEY})
        if response.status_code == 200:
            response_data = json.loads(response.text)
            return response_data['items']
        raise ConnectionError
