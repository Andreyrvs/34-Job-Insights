from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)

    industries = {}
    for row in jobs:
        content = row["industry"]
        if content not in industries:
            industries[content] = 0
        industries[content] += 1

    remove_empty = list(filter(None, industries))
    return remove_empty


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_industry = []
    for industries in jobs:
        if industries["industry"] == industry:
            filtered_industry.append(industries)

    return filtered_industry
