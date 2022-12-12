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
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or str(job["min_salary"]).isdigit() is False
        or str(job["max_salary"]).isdigit() is False
        or int(job["min_salary"]) > int(job["max_salary"])
    ):
        raise ValueError("Ta tudo Errado 👽👽👽👽")

    try:
        if (
            int(salary) >= int(job["min_salary"])
            and int(salary) <= int(job["max_salary"])
        ):
            return True
        else:
            return False
    except TypeError:
        raise ValueError('O min_salary')


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
