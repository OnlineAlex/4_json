import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def pretty_print_json(json_file):
    format_data = json.loads(json_file)
    return json.dumps(format_data, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    link_file = sys.argv[1]
    json_file = load_data(link_file)
    print(pretty_print_json(json_file))
