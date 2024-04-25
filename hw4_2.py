from pathlib import Path
from colorama import Fore


def get_cats_info(path=None):
    if type(path) != str:
        return Fore.RED + 'Invalid path!'
    else:
        path = Path(path)
    try:
        with open(path, encoding='utf-8') as fh:
            data_cats_list = []
            for i in fh:
                keys = ['id', 'name', 'age']
                values = i.strip().split(',')
                data_cats_list.append({k: v for (k, v) in zip(keys, values)})
            return data_cats_list
    except FileNotFoundError:
        return Fore.RED + f"File '{path}' is not found!"


cats_info = get_cats_info('C:\Prodjects\h_w4\cats_file.txt')
print(cats_info)
