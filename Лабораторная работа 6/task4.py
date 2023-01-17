import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimiter=',', new_line='\n') -> list[dict]:
        with open(file) as f:
        heading = f.readline().strip(new_line).split(delimiter)
        lst = []
        for i in f:
            lst += [dict(zip(heading, i.strip(new_line).split(delimiter)))]
        return lst


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
#  для сохранения последней строки
