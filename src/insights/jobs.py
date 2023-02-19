from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    print(path)
    with open(path, encoding="utf-8") as file:

        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        array = list(jobs_reader)
    return array


def get_unique_job_types(path: str):
    jobs = read(path)

    job_types = {}
    for row in jobs:
        content = row["job_type"]
        if content not in job_types:
            job_types[content] = 0
        job_types[content] += 1

    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_job = []
    for all_jobs in jobs:
        if all_jobs["job_type"] == job_type:
            filtered_job.append(all_jobs)

    return filtered_job
