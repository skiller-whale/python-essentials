import csv
import os

dir_path = os.path.dirname(os.path.abspath(__file__))


CURRICULUM_PATH = os.path.dirname(dir_path)
DATA_PATH = os.path.join(CURRICULUM_PATH, 'data')
FEMALE_FILE = os.path.join(DATA_PATH, 'popular_female_names_1990s.csv')
MALE_FILE   = os.path.join(DATA_PATH, 'popular_male_names_1990s.csv')


def _read_csv(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        return list(reader)


def _read_name_list(path):
    name_data = _read_csv(path)
    return [item['Name'] for item in name_data]


girls_names = _read_name_list(FEMALE_FILE)
boys_names = _read_name_list(MALE_FILE)
