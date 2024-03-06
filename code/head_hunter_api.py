import json
import os

import requests

from code.hh_abstract import HhAbstract


class HeadHunterAPI(HhAbstract):
    """
    Класс, который получает информацию о вакансиях hh.ru
    """
    API_KEY = os.getenv('API_HH')

    def getting_vacancies(self, text: str):
        """
        :param text: профессия
        :return: Информацию о вакансиях
        """

        params = {'area': 113,
                  'text': text}
        url = f'https://api.hh.ru/vacancies'
        response = requests.get(url, params=params, headers={'apikey': self.API_KEY})
        response_data = json.loads(response.text)
        vacancies = []
        for vacancy in response_data['items']:
            if vacancy['salary']:
                vacancy_dict = {
                    'name': vacancy['name'],
                    'url': vacancy['url'],
                    'salary': vacancy['salary']['from'],
                    'area': vacancy['area']['name'],
                    'published_at': vacancy['published_at']
                }
                vacancies.append(vacancy_dict)
            else:
                vacancy_dict = {
                    'name': vacancy['name'],
                    'url': vacancy['url'],
                    'salary': vacancy['salary'],
                    'area': vacancy['area']['name'],
                    'published_at': vacancy['published_at']
                }
                vacancies.append(vacancy_dict)

        return vacancies

