from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)

    salaries = []
    for row in jobs:
        content = row["max_salary"]
        if content != "":
            salaries.append(content)

    convert_to_integer = [
        int(number) for number in salaries if number.isdigit()
    ]

    max_salary = convert_to_integer[0]
    for number in convert_to_integer:
        if number > max_salary:
            max_salary = number

    return max_salary


def get_min_salary(path: str) -> int:
    jobs = read(path)

    salaries = []
    for row in jobs:
        content = row["min_salary"]
        if content != "":
            salaries.append(content)

    convert_to_integer = [
        int(number) for number in salaries if number.isdigit()
    ]

    min_salary = convert_to_integer[0]
    for number in convert_to_integer:
        if number < min_salary:
            min_salary = number

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Não tem as chaves necessarias")
    elif (
        type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
    ):
        raise ValueError("Os valores devem ser inteiros")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary é maior que max_salary")
    try:
        range_minus = int(salary) >= int(job["min_salary"])
        range_plus = int(salary) <= int(job["max_salary"])
        range_of_salary = range_plus and range_minus
        return range_of_salary
    except TypeError:
        print("🔥🔥🔥🔥🔥🔥🔥")
        pass


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass

    return filtered_jobs
