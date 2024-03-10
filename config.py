from os import path

parent_dir = path.dirname(path.abspath(__file__))
VACANCIES_FILE = path.join(parent_dir, 'data', 'vacancies.json')
TEST_VACANCIES_FILE = path.join(parent_dir, 'tests', 'test_vacancies.json')
