from pathlib import Path


def total_salary(path) -> tuple:

    p = Path(path)
    total = 0
    average = 0
    if not p.exists():
        print(f"File '{p}' is not found!")
        return total, average
    else:
        with open(p, encoding='utf-8') as fh:
            salary_list = [int(i.strip().split(',')[1])
                           for i in fh.readlines()]
            for i in salary_list:
                total += i
            average = round(total / len(salary_list), 2)
        return total, average


total, average = total_salary('list_worker.txt')
print(
    f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
