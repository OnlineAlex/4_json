import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        parsed_json = json.loads(file.read())
        return parsed_json


def pretty_print_json(raw_data):
    pretty_json = json.dumps(raw_data, ensure_ascii=False, indent=4)
    print(pretty_json)


if __name__ == '__main__':
    try:
        json_file = sys.argv[1]
        json_data = load_data(json_file)
    except IndexError:
        print('Ошибка! Вы не указали путь к файлу JSON.')
        print('Сработает, если написать "python pprint_json.py <путь к файлу>"')
    except FileNotFoundError:
        print('Ошибка! Система не нашла такой файл.')
        print('Пробуйте указать полный путь к файлу.')
    except ValueError:
        print('Ошибка. Файл должен быть в формате JSON.')
    else:
        pretty_print_json(json_data)
