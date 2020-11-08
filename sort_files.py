import os
import shutil

PATH = r"C:/FOLDER/PATH/HERE"


def get_info_files(location: str) -> dict:
    data = {}
    files = os.listdir(location)
    for file in files:
        if os.path.isfile(os.path.join(location, file)):
            _, ex = os.path.splitext(file)
            ex = '@{}'.format(ex[1:].lower())
            if ex in data.keys():
                data[ex].append(file)
            else:
                data[ex] = []
                data[ex].append(file)

    return data


def create_directories(location: str, names: list):
    files = os.listdir(location)
    for name in names:
        if name not in files:
            os.mkdir(os.path.join(location, name))
    return


def move_to_directories(location: str, data: dict):
    keys = data.keys()
    for key in keys:
        for file in data[key]:
            current = os.path.join(location, file)
            destination = os.path.join(location, key, file)
            shutil.move(current, destination)
    return


def print_report(data: dict):
    report = ['---- REPORT ----']
    amount = 0
    for ext in data.keys():
        size = len(data[ext])
        amount += size
        report.append("{} : {} files".format(ext[1:], size))
    report.append('-- END REPORT --')
    for line in report:
        print(line)
    return


info = get_info_files(PATH)
create_directories(PATH, info.keys())
move_to_directories(PATH, info)
print_report(info)
