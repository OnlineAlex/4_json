import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def pretty_print_json(json_str):
    try:
        parsed_str = json.loads(json_str)
    except ValueError:
        return 'Ошибка. Файл должен біть в формате JSON'

    return json.dumps(parsed_str, ensure_ascii=False, indent=4)


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
    else:
        print(pretty_print_json(json_data))
